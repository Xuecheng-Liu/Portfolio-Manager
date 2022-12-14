# import pandas_datareader.data as web
# import datetime
# import pandas as pd
#
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
#
# start = datetime.datetime(2019,9,15)
# end = datetime.datetime(2021,9,15)
#
# def get_stock(ticker):
#     data = web.DataReader(f"{ticker}","yahoo",start,end)
#     data[f'{ticker}'] = data["Close"]
#     data = data[[f'{ticker}']]
#     print(data.head())
#     return data
#
# #pfizer = get_stock("PFE")
#
# from functools import reduce
#
#
# def combine_stocks(tickers):
#     data_frames = []
#     for i in tickers:
#         data_frames.append(get_stock(i))
#
#     df_merged = reduce(lambda left, right: pd.merge(left, right, on=['Date'], how='outer'), data_frames)
#     print(df_merged.head())
#     return df_merged


# stocks = ["MRNA", "PFE", "JNJ"]
# combine_stocks(stocks)


# portfolio = combine_stocks(stocks)
#
# portfolio.to_csv("portfolio.csv", index=False)
# portfolio = pd.read_csv("portfolio.csv")

from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
import yfinance as yf

tickers = ["MRNA", "PFE", "JNJ", "GOOGL",
           "AAPL", "COST", "WMT", "KR", "JPM",
          "BAC"]
df = yf.download(tickers=tickers,period="max",interval="1d")['Close'].iloc[-30:,:]

mu = mean_historical_return(df)
S = CovarianceShrinkage(df).ledoit_wolf()

print(mu)
print(S)
# from pypfopt.efficient_frontier import EfficientFrontier
#
# ef = EfficientFrontier(mu, S)
# weights = ef.efficient_return(0.5)
#
# cleaned_weights = ef.clean_weights()
# print(dict(cleaned_weights))
# ef.portfolio_performance(verbose=True)