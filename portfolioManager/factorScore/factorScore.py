# functions to the stock based on factors
'''
This is the factor module for getting factor value for inner-sector stocks, and give their score for each factor respectively.
'''
import yfinance as yf
import pandas as pd
import numpy as np

def get_sector_factor_table(sector_ticker):
    '''
    return an empty dataframe with sector top 10 components as index
    This prepares for storing stock's factor value
    '''
    # initiate sector components
    sector_compo = []
    sector_info = yf.Ticker(sector_ticker).info['holdings']
    for i in range(len(sector_info)):
        sector_compo.append(sector_info[i]['symbol'])
    sector_columns = ['dividend_rate', 'operating_CF', 'market_cap','ROE', 'PB']
    sector_table = pd.DataFrame(index=sector_compo, columns=sector_columns)
    sector_table.index = sector_compo
    # add factors values: dividend_rate, roe2pb, cf2p12
    factors = ['trailingAnnualDividendRate', 'operatingCashflow', 'marketCap', 'returnOnEquity','priceToBook']
    for ticker in sector_table.index:
        ticker_info = yf.Ticker(ticker).info
        for j in range(len(factors)):
            if factors[j] in ticker_info:
                sector_table.loc[ticker, sector_columns[j]] = ticker_info[factors[j]]
    # calculate factor and assgin scores
    sector_table['ROE2PB'] = sector_table['ROE'] / sector_table['PB']
    sector_table['CF2P12'] = sector_table['operating_CF'] / sector_table['market_cap']
    factor_columns = ['dividend_rate', 'ROE2PB', 'CF2P12']
    sector_factor_table = sector_table[factor_columns]
    for k in range(len(factor_columns)):
        sector_factor_table.sort_values(by = factor_columns[k], inplace=True)
        sector_factor_table[factor_columns[k] + '_score'] = [ i for i in range(1, 11)]
        sector_factor_table[factor_columns[k] + '_score'][sector_factor_table[factor_columns[k]].isnull()] = 0
            
    sector_factor_table['Total_Score'] = sector_factor_table.iloc[:, [3,4,5]].sum(axis = 1)
    sector_factor_table.sort_values(by = 'Total_Score', ascending = False, inplace=True)
    return sector_factor_table
 
def get_sector_stock(n, sectors_list):
    stock_list = []
    #sector_ticker_list = ['XLB','XLC','XLE','XLF','XLI','XLK','XLP','XLRE','XLU','XLV','XLY']
    for sector_ticker in sectors_list:
        table = get_sector_factor_table(sector_ticker)
        sector_factor_table_dict[sector_ticker] = table
        stocks = list(table.index[:n])
        for i in range(len(stocks)):
            stock_list.append(stocks[i])
    return stock_list
  
stock_list = get_sector_stock(2, ['XLF', 'XLB'])
stock_list
