# This script downloads historical stock data (2020 to date) for specified stocks.
# It calculates monthly financial metrics including TSR, Volatility (both normal and 252-day rolling), 
# and Sharpe Ratio (both normal and rolling) for each month from 2020 to date.
# The rolling calculations use a 252-day lookback window to provide more stable, long-term risk assessment,
# while normal calculations use only the current month's data for short-term performance tracking.
# This results in granular monthly data, providing up to 72 rows per stock (12 months × 6 years),
# essential for detailed month-over-month and year-over-year performance analysis.
# Results are exported to a Microsoft SQL Server database (table: stock_metrics_monthly) and a timestamped CSV file.


import yfinance as yf
import os
import pandas as pd
import pyodbc
import pandas
from sqlalchemy import create_engine
from datetime import datetime
import calendar
from config import  STOCK_TICKERS, START_DATE, END_YEAR, DB_NAME, DB_SERVER, TABLE_STOCK_MONTHLY

def get_rolling_daily_return(stock, end_date, window_days = 252):   #defines a rolling daily return function to be called and used to calculate monthly sharpe
    data_up_to_date = stock[stock.index <= end_date]                 #Filters the DataFrame to include only data from the beginning up to and including end_date   
    rolling_data =  data_up_to_date.tail(window_days)               #Takes the last N rows from the filtered data, where N = window_days (252 by default)
    daily_returns = rolling_data['Close'].pct_change().dropna()        #Calculates percentawge change between consecutive closing prices in the rolling window, and drop any nan value
    return  daily_returns                                           #Returns the Series of daily returns (252 values) back to wherever the function is called.


tickers = STOCK_TICKERS
data =[]                   
for ticker in tickers:
    print(f'downloading {ticker}')
    stock = yf.download(ticker, start=START_DATE)        #gets stocks from 2020
    print(f'getting {ticker} info')
    symbol = ticker                                        #defines a variable holding ticker string as symbol                        
    ticker_object = yf.Ticker(symbol)                      #creates a ticker object which holds all data for a specified stock whose ticker is assigned to symbol
    info = ticker_object.info                              #this calls the info property of the ticker object
    sector = info.get('sector')                            #extracts the value associated with the key 'sector' from the info dictionary
    industry = info.get('industry')                        #extracts the value associated with industry, usually more specific industry sub category
    company_name = info.get('longName')                    #extracts the the name of the company that owns the stock
    dividend_history = ticker_object.dividends             #this extracts the dividend history of the stock, gets only rows where dividends were paid
    #Dividend History Timezone Normalization:
    #yfinance returns dividend history with a timezone-aware DatetimeIndex.
    #We strip the timezone so we can filter by .index.year and .index.month
    #without pandas throwing errors when combining conditions with &
    if not dividend_history.empty:
        dividend_history.index = dividend_history.index.tz_convert(None)
    stock_data = ticker_object.history(start='2020-01-01')  #this extracts stocks history, includes rows for stocks with no dividends
    outstanding_shares = info.get('sharesOutstanding')      #gets current share
   
    for year in range(2020, END_YEAR +1):                  #for each year
        year_data = stock[stock.index.year==year]   #process only the current year in loop, and get only that year's data
        yearly_daily_volatility = year_data['Close'].std()
        annual_volatility = yearly_daily_volatility * (len(year_data)**0.5) #length of year data gets how many days are in a trading year, which is usually 252 
        if year_data.empty or len(year_data)<2:     
            continue
        for month in range(1, 13):
            month_data = stock[(stock.index.year ==year) & (stock.index.month == month)]
            if month_data.empty or len(month_data) < 2:
                continue
            closing_price = month_data['Close']
            first_close = closing_price.iloc[0]
            last_close = closing_price.iloc[-1]
            monthly_dividends = dividend_history[(dividend_history.index.year == year) & 
                                               (dividend_history.index.month == month)]
            monthly_dividends_total = monthly_dividends.sum()
            monthly_tsr = ((last_close - first_close) + monthly_dividends_total)/ first_close
            month_last_day = month_data.index[-1]                     #Gets the last trading day of the month from the index

            #Call the function we created above: Pass the entire stock dataset, Pass the last day of the current month as the end point and Request 252 days of history
            rolling_daily_return = get_rolling_daily_return(stock, month_last_day, window_days=252)
            daily_volatility = rolling_daily_return.std()                           #Calculates standard deviation of the 252 daily returns.
            monthly_volatility_rolling = daily_volatility * (len(month_data)**0.5)  #Scales daily volatility to monthly volatility using the square root of time rule.
            monthly_sharpe_ratio_rolling = monthly_tsr / monthly_volatility_rolling #Long-term risk-adjusted performance (standard)

            monthly_daily_return = closing_price.pct_change()
            monthly_daily_volatility = monthly_daily_return.std()
            monthly_volatility = monthly_daily_volatility * (len(month_data)**0.5)  #length of month data gets how many trading days are in a month, which is usually 21    
            monthly_sharpe_ratio = monthly_tsr / monthly_volatility    # Short-term month-specific risk-adjusted performance

            month_name = calendar.month_name[month]                     #get month name

            #check if month in loop is less than current month, if it is, then true, month is complete, otherwise, false, month is not complete
            is_month_complete =  (year < datetime.now().year) or (year == datetime.now().year and month < datetime.now().month)
            if is_month_complete:
                is_month_complete = 'yes'
            elif is_month_complete == False:
                is_month_complete = 'no'
            #create a dataframe
            monthly_data = pd.DataFrame({'Ticker': ticker,
                                     'Year': year,
                                     'Month': month,
                                     'MonthName': month_name,
                                     'Company_Name': company_name,  
                                     'Sector': sector,             
                                     'Monthly_TSR': round(monthly_tsr, 4),
                                     'MonthlyVolatility' : round(monthly_volatility, 4),
                                     'MonthlyVolatiltyRolling': round(monthly_volatility_rolling, 4),
                                     'MonthlySharpe': round(monthly_sharpe_ratio, 2),
                                     'MonthlySharpeRolling': round(monthly_sharpe_ratio_rolling, 2),
                                     'FirstClose': round(first_close, 4),
                                     'LastClose': round(last_close, 4),
                                     'TradingDays': len(month_data),
                                     'CompleteMonth' : is_month_complete,
                                     'LastUpdated': datetime.now() }
                                     )
            data.append(monthly_data)
final_data = pd.concat(data, ignore_index=True)
final_data

#saving to microsoft server

#create connection string, after importing pyodbc and from sqlalchemy, importing create_engine-- these are language tranlators to write to sql server
connection_str = f'mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+Sql+Server&trusted_connection=yes'
engine = create_engine(connection_str)     
print('Inserting Data into Sql Server')
final_data.to_sql(TABLE_STOCK_MONTHLY, engine, if_exists= 'replace', index=False) #load to Sql Server

print(f'{len(final_data)} rows of stock data added to MS server')


#saving the data as csv with timestamps
directory = r'c:\Users\user\stock_metrics_pipeline\cv_save'
timestamp = datetime.now()
timestamp = timestamp.strftime('%Y_%m_%d__%H_%M_%S')    #format timestamp to string 
filename = f'stock_metrics_monthly {timestamp}.csv'
final_data.to_csv(os.path.join(directory, filename), index=False) #to be saved in the directory path
print(f'{len(final_data)} rows of stock data saved successfully to {directory}')

         

