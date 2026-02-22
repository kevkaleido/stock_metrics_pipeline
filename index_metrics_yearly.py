# This script downloads historical index data (2020 to date) for specified market indices.
# It calculates yearly financial metrics including TSR, Volatility, and Sharpe Ratio for each year from 2020 to date.
# Additional metrics include Max and Min daily profit and their corresponding dates, and total trading days per year.
# This results in granular yearly data, providing up to 7 rows per index (1 row per year),
# essential for benchmarking and year-over-year performance analysis across major market indices.
# Results are exported to a Microsoft SQL Server database (table: index_metrics_yearly) and a timestamped CSV file.

import yfinance as yf
import os
import pandas as pd
import pyodbc
import pandas
from sqlalchemy import create_engine
from datetime import datetime
from config import INDEX_TICKERS,START_DATE, END_YEAR, DB_NAME, DB_SERVER, TABLE_INDEX_YEARLY

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
    for year in range(2020, END_YEAR + 1):
        year_data = index_data[index_data.index.year == year]
        if year_data.empty or len(year_data)< 2:
            continue
        print(f'Calculating {year} {ticker} metrics for {name}')
        closing_prices = year_data['Close'].squeeze()    ##adding .squeeze() so I will always get scaler values instead of series
        first_close = closing_prices.iloc[0]
        last_close = closing_prices.iloc[-1]
        daily_returns = closing_prices.pct_change()      
        annual_tsr =  (last_close - first_close)/ first_close  
        daily_volatility = daily_returns.std()
        annual_volatility = daily_volatility * (len(year_data)**0.5)
        sharpe_ratio = annual_tsr / annual_volatility
        
        #check if year is complete
        is_complete = year < (datetime.now().year)
     
    #create a dataframe to save metrics values in
        print(f'Creating DataFrame for {year} {ticker} for {name}')
        metrics_data = pd.DataFrame({'Ticker': ticker,
                                    'Year' : year,
                                    'Index_Name': name,
                                    'Region': info.get('region'),
                                    'Annual_TSR' : round(annual_tsr,4),
                                    'AnnualVolatility': round(annual_volatility,4),
                                    'Sharpe_Ratio' : round(sharpe_ratio, 2),
                                    'MaxDailyProfit': daily_returns.max(),
                                    'MaxDP_Date': daily_returns.idxmax().strftime('%Y-%m-%d'),
                                    'MinDailyProfit': daily_returns.min(),
                                    'MinDP_Date': daily_returns.idxmin().strftime('%Y-%m-%d'),
                                    'TradingDays': len(year_data),
                                    'YearComplete': is_complete,
                                    'LastUpdated': datetime.now()
                                 }, index = [0])
    
        data.append(metrics_data)
        final_data = pd.concat(data)
final_data
    

#saving to microsoft server

#create connection string, after importing pyodbc and from sqlalchemy, importing create_engine-- these are language tranlators to write to sql server
connection_str = f'mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+Sql+Server&trusted_connection=yes'
engine = create_engine(connection_str)     
print('Inserting Data into Sql Server')
final_data.to_sql(TABLE_INDEX_YEARLY, engine, if_exists= 'replace', index=False) #load to Sql Server

print(f'{len(final_data)} rows of index data added to MS server')


#saving the data as csv with timestamps
directory = os.getcwd()
timestamp = datetime.now()
timestamp = timestamp.strftime('%Y%m%d_%H%M%S')    #format timestamp to string 
filename = f'index_metrics_yearly{timestamp}.csv'
final_data.to_csv(filename, index=False)
print(f'{len(final_data)} rows of index data saved successfully to {directory}')