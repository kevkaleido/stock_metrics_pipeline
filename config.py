
from datetime import datetime
from Stocks_and_Indices import ALL_STOCKS, ALL_INDICES

# STOCKS & INDICES
STOCK_TICKERS = ALL_STOCKS

INDEX_TICKERS = ALL_INDICES

# DATE RANGE
START_DATE = "2020-01-01"
END_YEAR = datetime.now().year  # always current year


# DATABASE
DB_SERVER = r"localhost\SQLEXPRESS"
DB_NAME = "StockIndex"
DB_DRIVER = "ODBC+Driver+17+for+SQL+Server"

# TABLE NAMES
TABLE_STOCK_MONTHLY  = "stock_metrics_monthly"
TABLE_STOCK_YEARLY   = "stock_metrics_yearly"
TABLE_INDEX_MONTHLY  = "index_metrics_monthly"
TABLE_INDEX_YEARLY   = "index_metrics_yearly"

