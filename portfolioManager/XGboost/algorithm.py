"""
This module contains a function that implements the XGBoost algorithm for regression.
"""
import yfinance as yf
import talib as ta
import pandas as pd
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor


def xgb_model(ticker):
    """
    This function implements the XGBoost algorithm for regression.
    :param ticker: an abbreviation used to identify a particular stock
    """
    if yf.Ticker(ticker).info['regularMarketPrice'] is None:
        raise ValueError("please enter valid ticker")

    data = yf.download(tickers=ticker, period="max", interval="1d")
    data = data.drop('Adj Close', axis=1)
    data['Return'] = ((data['Close'] / data['Close'].shift(1)) - 1) * 100
    data = data.dropna()

    data['SMA10'] = ta.SMA(data['Close'], timeperiod=10)
    data['SMA30'] = ta.SMA(data['Close'], timeperiod=30)
    data['SMA200'] = ta.SMA(data['Close'], timeperiod=200)
    data['EMA10'] = ta.EMA(data['Close'], timeperiod=10)
    data['EMA30'] = ta.EMA(data['Close'], timeperiod=30)
    data['EMA200'] = ta.EMA(data['Close'], timeperiod=200)
    data['MOM10'] = ta.MOM(data['Close'], timeperiod=10)
    data['MOM30'] = ta.MOM(data['Close'], timeperiod=30)
    data['MOM200'] = ta.MOM(data['Close'], timeperiod=200)
    data['RSI10'] = ta.RSI(data['Close'], timeperiod=10)
    data['RSI30'] = ta.RSI(data['Close'], timeperiod=30)
    data['RSI200'] = ta.RSI(data['Close'], timeperiod=200)
    data['K10'], data['D10'] = ta.STOCH(data['High'], data['Low'], data['Close'], fastk_period=10)
    data['K30'], data['D30'] = ta.STOCH(data['High'], data['Low'], data['Close'], fastk_period=30)
    data['K200'], data['D200'] = ta.STOCH(data['High'], data['Low'], data['Close'], fastk_period=200)

    data['Return-1'] = data['Return'].shift(-1)
    data['Return-2'] = data['Return'].shift(-2)
    data['Return-3'] = data['Return'].shift(-3)
    data['Return-4'] = data['Return'].shift(-4)
    data['Return-5'] = data['Return'].shift(-5)

    X_train = data['2015-01-01':].iloc[0:-5, 0:-5]
    y_train = data['2015-01-01':].iloc[0:-5, -5:]
    X_pred = data['2015-01-01':].iloc[-1:, 0:-5]

    xgb = XGBRegressor()
    mreg = MultiOutputRegressor(xgb).fit(X_train, y_train)
    y_pred = pd.DataFrame(mreg.predict(X_pred), index=[ticker], columns=['Day1', 'Day2', 'Day3', 'Day4', 'Day5'])

    return y_pred
