from XGboost import xgb_model
from visualization import plot


ticker_list = ["XLB","XLC","XLE","XLF","XLI","XLK","XLP","XLRE","XLU","XLV","XLY"]
for ticker in ticker_list:
  plot(xgb_model(ticker))

  
ticker_list = ['DOW', 'APD', 'GOOGL', 'T', 'PXD']
weight_list = [0.13, 0.28, 0.45, 0.10, 0.04]
backtest(ticker_list, weight_list)
