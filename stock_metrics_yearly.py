# This script downloads historical stock data (2020 to date) for specified stocks.
# It calculates yearly financial metrics including TSR, Annualized Volatility, and Sharpe Ratio for each year from 2020 to date.
# Dividend history is factored into TSR to reflect true total shareholder return.
# Additional metrics include Max and Min daily profit and their corresponding dates, Market Cap approximation,
# Sector, Industry, and total trading days per year.
# This results in granular yearly data, providing up to 6 rows per stock (1 row per year),
# essential for detailed year-over-year performance analysis.
# Results are exported to a Microsoft SQL Server database (table: stock_metrics_yearly) and a timestamped CSV file.


import yfinance as yf
import os
import pandas as pd
import pyodbc
import pandas
from sqlalchemy import create_engine
from datetime import datetime

from config import STOCK_TICKERS, START_DATE, END_YEAR, DB_NAME, DB_SERVER, TABLE_STOCK_YEARLY



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
    dividend_history = ticker_object.dividends             #this extracts the dividend history of the stock
    dividend_history = ticker_object.dividends             #this extracts the dividend history of the stock, gets only rows where dividends were paid
    #Dividend History Timezone Normalization:
    #yfinance returns dividend history with a timezone-aware DatetimeIndex.
    #We strip the timezone so we can filter by .index.year
    #without pandas throwing errors when combining conditions with &
    if not dividend_history.empty:
        dividend_history.index = dividend_history.index.tz_convert(None)
    outstanding_shares = info.get('sharesOutstanding')      #gets current share
    for year in range(2020, END_YEAR +1):                  #for each year
        year_data = stock[stock.index.year==year]   #process only the current year in loop, and get only that year's data
        if year_data.empty or len(year_data)<2:     
            continue
        print(f'Calculating {year} {ticker} metrics for {company_name}')
        closing_prices = year_data['Close'].squeeze()        #adding .squeeze() so I will always get scaler values from standard deviations and the likes, instead of series, will need to add an index to dataframe because If using all scalar values, you must pass an index
        if closing_prices.empty or len(closing_prices) == 0:   #an if condition to avoid any error that would stop the entire loop, if a stock close series is empty, ignore and move to another  
            continue
        last_close = closing_prices.iloc[-1] 
        first_close = closing_prices.iloc[0]

        yearly_dividends = dividend_history[dividend_history.index.year == year].sum()   #calculates the sum of yearly dividend history
        annual_tsr = ((last_close - first_close) + yearly_dividends) / first_close #this now becomes annual total shareholder return since we are calculating by year_data
        daily_return = closing_prices.pct_change() 
        daily_volatility = daily_return.std()                   #high volatility means more risk
        
 
    #annualized volatility is the square root of trading days in a year multiplied by daily volatility    
        annualized_volatility = daily_volatility * (len(year_data)**0.5)

     
    #get market cap approximation using outstanding shares
        if outstanding_shares:
            market_cap = outstanding_shares * last_close
        else:
            market_cap = None

    #Sharpe ratio measures the return earned per unit of risk(volatility)
    #if the sharpe ratio is less than 1.0, the stocks return is low compared to its risk
        if annualized_volatility.squeeze() !=0:           #adding squeeze gets a scaler value
            sharpe_ratio = annual_tsr/annualized_volatility 
        else:
            sharpe_ratio =None
        

    #get max and min profit per year includind days it happened
        max_daily_profit = daily_return.max()
        max_daily_profit_date = daily_return.idxmax()        #get the index where daily return is max
        min_daily_profit = daily_return.min()
        min_daily_profit_date = daily_return.idxmin()        #get the index where daily return in minimum

    #check if current year in loop is less than current year, if it is, then true, year is complete, otherwise, false, year is not complete
        is_complete = (year < datetime.now().year)


    #create a dataframe 
        print(f'Creating Dataframe for {year} {company_name} {ticker} stock for ')   
        new_data=pd.DataFrame({'Ticker': ticker,
                               'Year': year,
                               'CompanyName': company_name,
                               'Annual_TSR': round(annual_tsr, 4),
                               'AnnualVolatility': round(annualized_volatility,  4),
                               'SharpeRatio': round(sharpe_ratio, 2),
                               'MaxDailyProfit': round(max_daily_profit, 4),
                               'MaxDP_Date': max_daily_profit_date,
                               'MinDailyProfit': round(min_daily_profit, 4),
                               'MinDP_Date': min_daily_profit_date,
                               'MarketCap': market_cap,
                               'Sector': sector,
                               'industry': industry,
                               'CompleteYear': is_complete,
                               'TradingDays': len(year_data),
                               'LastUpdated': datetime.now()}, index=[0])
        


    #append the dataframes to the formally empty list
        data.append(new_data)

    #concatenate all dataframes in the list    
        final_data = pd.concat(data)
        
final_data

#saving to microsoft server

#create connection string, after importing pyodbc and from sqlalchemy, importing create_engine-- these are language tranlators to write to sql server
connection_str = f'mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+Sql+Server&trusted_connection=yes'
engine = create_engine(connection_str)     
print('Inserting Data into Sql Server')
final_data.to_sql(TABLE_STOCK_YEARLY, engine, if_exists= 'replace', index=False) #load to Sql Server
print(f'{len(final_data)} rows of stock data added to MS server')



#saving the data as csv with timestamps
directory = r'c:\Users\user\stock_metrics_pipeline\cv_save'
timestamp = datetime.now()
timestamp = timestamp.strftime('%Y_%m_%d__%H_%M_%S')    #format timestamp to string 
filename = f'stock_metrics_yearly {timestamp}.csv'
final_data.to_csv(os.path.join(directory, filename), index=False) #to be saved in the directory path
print(f'{len(final_data)} rows of stock data saved successfully to {directory}')


