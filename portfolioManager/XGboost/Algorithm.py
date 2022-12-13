import yfinance as yf
import talib as ta
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor


def xgb_model(ticker):
    data = yf.download(tickers=ticker, period="max", interval="1d")
    data = data.drop('Adj Close', axis=1)
    data['Return'] = ((data['Close'] / data['Close'].shift(1)) - 1) * 100
    data = data.dropna()

    for i in range(1, 10):
        data['Open' + str(i)] = data['Open'].shift(i)
        data['High' + str(i)] = data['High'].shift(i)
        data['Low' + str(i)] = data['Low'].shift(i)
        data['Close' + str(i)] = data['Close'].shift(i)
        data['Volume' + str(i)] = data['Volume'].shift(i)
        data['Return' + str(i)] = data['Return'].shift(i)

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

    X_train = data['2010-01-01':].iloc[0:-5, 0:-5]
    y_train = data['2010-01-01':].iloc[0:-5, -5:]
    X_pred = data['2010-01-01':].iloc[-1:, 0:-5]

    xgb = XGBRegressor(gamma=0.1, learning_rate=0.01, max_depth=3,
                       min_child_weight=16, n_estimators=200, random_state=42)
    mreg = MultiOutputRegressor(xgb).fit(X_train, y_train)

    y_pred = mreg.predict(X_pred)

    return y_pred
