from XGboost import xgb_model
from visualization import plot


ticker_list = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]
for ticker in ticker_list:
    plot(xgb_model(ticker))
