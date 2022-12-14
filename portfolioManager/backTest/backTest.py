# to do
import pandas as pd
import yfinance as yf

def backtest(ticker_list, weight_list):
    stock_backtest = pd.DataFrame()
    for ticker in ticker_list:
        ticker_last5d_price = yf.download(tickers=ticker, period="max", interval="1d").iloc[-365:, :]['Close']
        ticker_last5d_ret = (ticker_last5d_price - ticker_last5d_price.shift(1)) / ticker_last5d_price.shift(1)
        ticker_last5d_ret.dropna(inplace=True)
        stock_backtest[ticker] = ticker_last5d_ret
    stock_weight = pd.DataFrame()
    stock_weight['weight'] = weight_list
    portfolio_return = stock_backtest.mul(stock_weight['weight'].values, axis=1)
    stock_backtest['daily_return'] = portfolio_return.sum(axis=1)

    # plot
    import matplotlib.pyplot as plt
    fontsize = 20
    font1 = {'size': fontsize}
    plt.figure(figsize=(15, 10))
    date = stock_backtest.index
    ret = stock_backtest['daily_return']
    plt.plot(date, ret, color="r", linestyle="-")
    plt.xlabel("Date", font1)
    plt.ylabel("Portfolio Daily Return", font1)
    plt.tick_params(labelsize=20)
    # plt.legend(loc="best",prop=font1)
    plt.title("Portfolio Back-Testing")
    plt.show()


# ticker_list = ['DOW', 'APD', 'GOOGL', 'T', 'PXD']
# weight_list = [0.13, 0.28, 0.45, 0.10, 0.04]
# backtest(ticker_list, weight_list)
