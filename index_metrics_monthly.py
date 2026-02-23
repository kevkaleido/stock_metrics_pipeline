# This script downloads historical index data (2020 to date) for specified market indices.
# It calculates monthly financial metrics including TSR, Volatility (both normal and 252-day rolling),
# and Sharpe Ratio (both normal and rolling) for each month from 2020 to date.
# The rolling calculations use a 252-day lookback window to provide more stable, long-term risk assessment,
# while normal calculations use only the current month's data for short-term performance tracking.
# Unlike stocks, indices do not pay dividends, so TSR is based purely on price returns.
# This results in granular monthly data, providing up to 84 rows per index (12 months × 7 years),
# essential for benchmarking stock performance against major market indices on a month-over-month
# and year-over-year basis.
# Results are exported to a Microsoft SQL Server database (table: index_metrics_monthly) and a timestamped CSV file.

import yfinance as yf
import os
import pandas as pd
import pyodbc
import pandas
from sqlalchemy import create_engine
from datetime import datetime
import calendar
from config import INDEX_TICKERS,START_DATE, END_YEAR, DB_NAME, DB_SERVER, TABLE_INDEX_MONTHLY



def get_rolling_daily_return(index, end_date, window_days = 252):   #defines a rolling daily return function to be called and used to calculate monthly sharpe
    data_up_to_date = index_data[index_data.index <= end_date]            #Filters the DataFrame to include only data from the beginning up to and including end_date   
    rolling_data =  data_up_to_date.tail(window_days)           #Takes the last N rows from the filtered data, where N = window_days (252 by default)
    daily_returns = rolling_data['Close'].pct_change().dropna() #Calculates percentawge change between consecutive closing prices in the rolling window, and drop any nan value
    return  daily_returns                                       #Returns the Series of daily returns (252 values) back to wherever the function is called.
   
# Index tickers
index_tickers = INDEX_TICKERS
data = []                                 
# Download index data 
for ticker in index_tickers:
    print(f'Downloading {ticker}')
    index_data = yf.download(ticker, start=START_DATE)
    print(f'getting {ticker} info')
    index_ticker_object = yf.Ticker(ticker)
    info = index_ticker_object.info
    name = info.get('longName')       

    for year in range(2020, END_YEAR +1):
        year_data = index_data[index_data.index.year == year]
        if year_data.empty or len(year_data)< 2:
            continue
        for month in range(1, 13):
            month_data = index_data[(index_data.index.year ==year) & (index_data.index.month == month)]
            if month_data.empty or len(month_data) < 2:
                continue
            closing_price = month_data['Close']
            first_close = closing_price.iloc[0]
            last_close = closing_price.iloc[-1]
            monthly_tsr = (last_close - first_close)/ first_close
            month_last_day = month_data.index[-1]                     #Gets the last trading day of the month

            #Call the function we created above: Pass the entire index dataset, Pass the last day of the current month as the end point and Request 252 days of history
            rolling_daily_return = get_rolling_daily_return(index_data, month_last_day, window_days=252)
            daily_volatility = rolling_daily_return.std()                           #Calculates standard deviation of the 252 daily returns.
            monthly_volatility_rolling = daily_volatility * (len(month_data)**0.5)  #Scales daily volatility to monthly volatility using the square root of time rule.
            monthly_sharpe_ratio_rolling = monthly_tsr / monthly_volatility_rolling #Long-term risk-adjusted performance (standard)

            monthly_daily_return = closing_price.pct_change()
            monthly_daily_volatility = monthly_daily_return.std()
            monthly_volatility = monthly_daily_volatility * (len(month_data)**0.5)  #length of month data gets how many trading days are in a month, which is usually 21    
            monthly_sharpe_ratio = monthly_tsr / monthly_volatility    # Short-term month-specific risk-adjusted performance
            

            #get month name
            month_name = calendar.month_name[month]  
            #check if month in loop is less than current month, if it is, then true, month is complete, otherwise, false, month is not complete
            is_month_complete =  (year < datetime.now().year) or (year == datetime.now().year and month < datetime.now().month)
            
            #create a dataframe
            monthly_data = pd.DataFrame({'Ticker': ticker,
                                     'Year': year,
                                     'Month': month,
                                     'Month_Name': month_name,
                                     'IndexName': name,              
                                     'Monthly_TSR': round(monthly_tsr, 4),
                                     'MonthlyVolatility' : round(monthly_volatility, 4), 
                                     'MonthlyVolatiltyRolling': round(monthly_volatility_rolling, 4),
                                     'MonthlySharpe': round(monthly_sharpe_ratio, 2),
                                     'MonthlySharpe_Rolling': round(monthly_sharpe_ratio_rolling, 2),
                                     'FirstClose': round(first_close, 4),
                                     'LastClose': round(last_close, 4),
                                     'Trading_Days': len(month_data),
                                     'CompleteMonth' : is_month_complete,
                                     'LastUpdated': datetime.now() }
                                     )
            data.append(monthly_data)
final_data = pd.concat(data, ignore_index=True)
final_data



#saving to microsoft server  

#create connection string, after importing pyodbc and from sqlalchemy, importing create_engine -- these are language tranlators to write to sql server
connection_str = f'mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+Sql+Server&trusted_connection=yes'
engine = create_engine(connection_str)     
print('Inserting Data into Sql Server')
final_data.to_sql(TABLE_INDEX_MONTHLY, engine, if_exists= 'replace', index=False) #load to Sql Server

print(f'{len(final_data)} rows of index data added to MS server')


#saving the data as csv with timestamps
directory = r'c:\Users\user\stock_metrics_pipeline\cv_save'
timestamp = datetime.now()
timestamp = timestamp.strftime('%Y_%m_%d__%H_%M_%S')    #format timestamp to string 
filename = f'index_metrics_monthly {timestamp}.csv'
final_data.to_csv(os.path.join(directory, filename), index=False) #to be saved in the directory path
print(f'{len(final_data)} rows of index data saved successfully to {directory}')
