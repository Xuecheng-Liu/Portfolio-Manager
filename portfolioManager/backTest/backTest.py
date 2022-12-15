'''
This is the backtest module for testing our constructed portfolio daily return during the past 12 month.
'''
import sys
import os

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def backtest(ticker_list, weight_list, path = None):
    '''
    Given a stock list and a weight list that assigned for stocks, generate a plot for
    daily return of the portfolio constructed from the stock and weight list.

    Parameters:
        ticker_list: a list that contains the stocks that the portfolio is constructed upon.
                     It should be returned from get_sector_stock funtion from factorScore.
        weight_list: a list that contains the weight than assigned for stocks in ticker_list.
                     It should be returned from calculate_weight function form meanVariance.
               path: optional parameter for giving the save path during testing.
    Return:
        generate a graph for plotting daily return of constructed portfolio during the past 12 month.
    '''
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

    fontsize = 20
    font1 = {'size': fontsize}
    plt.figure(figsize=(15, 10))
    date = stock_backtest.index
    ret = stock_backtest['daily_return']
    plt.plot(date, ret, color="r", linestyle="-")
    plt.xlabel("Date", font1)
    plt.ylabel("Portfolio Daily Return", font1)
    plt.tick_params(labelsize=20)
    plt.title("Portfolio Back-Testing")
    if path == None:
        plt.savefig(f'./static/backtest.jpg')
    else:
        plt.savefig(path + '/backtest_test.jpg')
