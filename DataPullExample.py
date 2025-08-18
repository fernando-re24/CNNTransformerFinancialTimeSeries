import IBKRSPull
import StockData

tickers = [
 'AAPL', 'MSFT', 'NVDA', 'AMZN', 'META', 'AVGO', 'GOOGL', 'TSLA', 'JPM', 'V',
 'COST', 'XOM', 'WMT', 'PG', 'JNJ', 'HD', 'ABBV', 'BAC', 'UNH', 'KO',
 'PM', 'CRM', 'ORCL', 'CSCO', 'GE', 'PLTR', 'ABT', 'MCD', 'CVX', 'LIN',
 'NOW', 'DIS', 'ACN', 'T', 'ISRG', 'MRK', 'UBER', 'GS', 'INTU', 'VZ',
 'AMD', 'ADBE', 'RTX', 'ENPH', 'APA', 'DVA', 'CZR', 'MHK', 'NWS', 'AMTM',
 'LMT', 'LOW', 'MS', 'NEE', 'NFLX', 'NKE', 'PEP', 'PFE', 'QCOM', 'SBUX',
 'SO', 'SPG', 'TGT', 'TMO', 'TMUS', 'TXN', 'UNP', 'UPS', 'USB', 'AMGN',
 'HPQ', 'GOOG', 'CAT', 'COP', 'DD', 'DUK', 'EMR', 'FDX', 'GD', 'GILD',
 'GM', 'HON', 'INTC', 'MMM', 'MO', 'AXP', 'CL', 'BBY', 'CF', 'BIIB',
 'CI', 'EW', 'RTX', 'MNST', 'ORLY', 'MCO', 'HUM', 'ADI', 'AON', 'AEP',
 'BDX', 'BSX', 'SPGI'
]

puller = IBKRSPull(7497, 2)
stocks_df = puller.pull_stocks(tickers)

data = StockData(stocks = stocks_df)

data.add_indicators()
data.create_sequences()
X_train, y_train, X_val, y_val, X_test, y_test = data.time_aware_split()