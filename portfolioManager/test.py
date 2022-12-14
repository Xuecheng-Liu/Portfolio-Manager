from XGboost import xgb_model
from visualization import plot

data = xgb_model("XLY")
plot(data)

# import sys
#
# print(sys.path[1]+"/portfolioManager/static")


# from meanVariance import calculate_weight
# tickers = ["MRNA", "PFE", "JNJ", "GOOGL",
#            "AAPL", "COST", "WMT", "KR", "JPM",
#            "BAC"]
#
# (calculate_weight(tickers, 0.5))

# from factorScore import get_sector_factor_table,get_sector_stock
# stock_list1 = get_sector_stock(2, ['XLF', 'XLB'])
# print(stock_list1)
