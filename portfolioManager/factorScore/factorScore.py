'''
This is the factorScore module for generate tables for sector and factor values for its component stocks,
and assign factor score for them.
Then select the highest n stocks from each sector that user selects to construct portfolio.
'''
import yfinance as yf
import pandas as pd


def get_sector_factor_table(sector_ticker):
    """
    Given the user's selected sector ticker, return a table than contains the sector
    component stocks and its factor value and scores.

    Parameter:
        sector_ticker: a single string that represents a sector ticker
    Return:
        sector_factor_tableL: a dataframe that contains sector components stock as its index, and factor values,
        factor scores and total scores and its columns.
    """
    sector_compo = []
    sector_info = yf.Ticker(sector_ticker).info['holdings']
    for i in range(len(sector_info)):
        sector_compo.append(sector_info[i]['symbol'])
    sector_columns = ['dividend_rate', 'operating_CF', 'market_cap', 'ROE', 'PB']
    sector_table = pd.DataFrame(index=sector_compo, columns=sector_columns)
    sector_table.index = sector_compo

    factors = ['trailingAnnualDividendRate', 'operatingCashflow', 'marketCap', 'returnOnEquity', 'priceToBook']
    for ticker in sector_table.index:
        ticker_info = yf.Ticker(ticker).info
        for j in range(len(factors)):
            if factors[j] in ticker_info:
                sector_table.loc[ticker, sector_columns[j]] = ticker_info[factors[j]]

    sector_table['ROE2PB'] = sector_table['ROE'] / sector_table['PB']
    sector_table['CF2P12'] = sector_table['operating_CF'] / sector_table['market_cap']
    factor_columns = ['dividend_rate', 'ROE2PB', 'CF2P12']
    sector_factor_table = sector_table[factor_columns]
    for k in range(len(factor_columns)):
        sector_factor_table.sort_values(by=factor_columns[k], inplace=True)
        sector_factor_table[factor_columns[k] + '_score'] = [i for i in range(1, 11)]
        sector_factor_table[factor_columns[k] + '_score'][sector_factor_table[factor_columns[k]].isnull()] = 0

    sector_factor_table['Total_Score'] = sector_factor_table.iloc[:, [3, 4, 5]].sum(axis=1)
    sector_factor_table.sort_values(by='Total_Score', ascending=False, inplace=True)
    return sector_factor_table


def get_sector_stock(n, sectors_list):
    '''
    Given user's input number of stock that should be selected from each sector and the sectors that user
    prefers, return a list that contains stock tickers that are selected from factor-scoring method.

    Parameters:
        n: an int represents the number of stock that users want to select from each sector
        sectors_list: a list represents the sectors that users want to select upon.
    Return:
        stock_list: a list that contains the tickers of the stocks that we wish users to construct portfolio upon.
    '''
    if n >= 11:
        raise ValueError("Number of stock you want to select from sectors cannot be larger than 10")
    if n == 1 and len(sectors_list) == 1:
        raise ValueError("Too few sectors and stocks! Please try again!")
    stock_list = []
    for sector_ticker in sectors_list:
        table = get_sector_factor_table(sector_ticker)
        stocks = list(table.index[:n])
        for i in range(len(stocks)):
            stock_list.append(stocks[i])
    return stock_list

