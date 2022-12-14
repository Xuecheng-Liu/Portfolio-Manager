from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
import yfinance as yf
from pypfopt.efficient_frontier import EfficientFrontier


# input: a list of tickers and expected return, return a dictionary with each ticker and weight
def calculate_weight(tickers, er):
    df = yf.download(tickers=tickers, period="max", interval="1d")['Close'].iloc[-30:, :]
    mu = mean_historical_return(df)
    S = CovarianceShrinkage(df).ledoit_wolf()
    ef = EfficientFrontier(mu, S)
    weights = ef.efficient_return(er)
    cleaned_weights = ef.clean_weights()
    ef.portfolio_performance(verbose=True)
    return dict(cleaned_weights)


