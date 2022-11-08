# User 1: Beginner Investor
Beginner Investors are defined as those who just beginner their investment life and do not have much knowledge about how the stock market goes. They would like using our application to get some historical stock data to do their own research or learn more about the market rather than using it as a investor advisor since they are likely to be cautious about stock return and relatively can tolerate no risk at market.


## Use Case
- Enter the tickers of stocks or sectors that he wants to explore along with the time window.
- (optional) Enter a ticker of benchmark, could be any stock or index
- Get a report about the stocks or sectors he entered, including a graph depicting historical return, return & risk analysis on indicators, and compare their performance with the benchmark (if any).

# User2: Sector Investor
Sector Investors are defined as those who are interested in invested their moeny in stocks that are in different sectors to control its risk. Thus, they are more concerned about how sectors perform rather than how some particular stocks' return perform. They would like to use our application for explore the historical or future trend for the sectors that he is interested in.

## Use Case:
-  Enter the tickers of the sectors that he is interested in along with the time window that can be set for both historical and forecasting uses.
-  (optional) Enter the ticker of a benchmark sector.
-  (optional) Enter the number of sectors that would be the most promising ones based on our application forecasting
-  Get a report about the sectors he entered, including a graph depicting historical and future return in the following days, return & risk analysis on indicators, compare their performance with the benmark (if any) and show the most promising sectors (if any) with their return forecasting.

# User3: Experienced Investor
Experienced Investors are defined as those who already develop their own insights about stock investment, have some basic knowledge about financial anaysis on company report, and know how market factors work for forecasting stock return. They would like to use our application to get some advice on how to construct a stock portfoliio to meet his expectation on return and outperform the benchmark.

## Use Case
- Enter the target return level and risk tolerance level that he has in mind.
- Select some market factors that he finds helpful for forecasting.
- Enter the ticker of benchmark index that he wishes to outperform.
- (optional) Enter the ticker of stocks or sectors that he thinks should be included in his portfolio.
- Get a report about a 10-stock portfolio that our application suggests he construct, including forecasting on future return & risk analysis, comparison with benchmark, and stock weight allocation. 




# Components
## Data Fetching
  - Fetch the market data from Yahoo Finance and store it in the csv files
## Feature Engineering
  - Process the raw data and add artificial features based on raw data for later training
## Model Setup
  - Use tensor flow to initilize the LSTM model
## Hyperparameter Tuning
  - Find the best number of hidden layer, number of neurons per layer and drop rate for the model
## Prediction Function
  - Use data fetching component to get the target input data and output the predicted return of stocks
## Factor Selction & Scoring Criteria
  - Select a particular factor and output the score of a particular stock
## Stock Ranking
  - Rank the stocks within a particular sector based on factor selection and calculation
## Portfolio Construction
  - Calculate the weight based on risk tolerance, expected return and target stocks.
## Graph Plotting
  - Given the stock ticker and plot the trend of that stock in different time horizons
## UI design
  - (to do)
