# User 1: Beginner Investor
Beginner Investors are defined as those who just beginner their investment life and do not have much knowledge about how the stock market goes. They would like using our application to get market forecasting or learn more about the market rather than using it as an investment advisor since they are likely to be cautious about stock return and relatively can tolerate no risk at market.


## Use Case
- Just click the 'Sector Forecasting' button and get a report about the stocks or sectors he entered, which includes 11 graghs for 11 sectors, respectively.

# User2: Experienced Sector Investor
Experienced sector investors are defined as those who are interested in invested their moeny in stocks that are in different sectors to control its risk. Thus, they are more concerned about how sectors perform rather than how some particular stocks' return perform. Those investors have developed their own insights about stock investment, have some basic knowledge about financial anaysis on company report, and know how market factors work for forecasting stock return. They would like to use our application for short-term investment reference to meet their expectation on return.

## Use Case:
-  Select the sectors that he is interested in along with the expected return and the number of stocks that he wish to select from each sectors.
-  Get a report about the portfolio we suggested he construct, including stocks weights, a graph depicting back-testing return analysis, risk and sharp ratio.



# Components
## Data Fetching
  - Fetch the market data from Yahoo Finance API and store it in csv format.
## Feature Engineering
  - Process the raw data and add artificial features based on raw data for later training
## Model Setup
  - Use tensor flow to initilize the LSTM model for stock return forecasting.
## Hyperparameter Tuning
  - Find the best number of hidden layer, number of neurons per layer and drop rate for the model.
## Prediction Function
  - Use data fetching component to get the target input data and output the predicted return of stocks.
## Factor Selction & Scoring Criteria
  - Given the user input factors and output the score of stocks in candidate sectors based on factor-scoring criteria.
## Stock Ranking
  - Rank the stocks within candidate sectors based on its factor scores.
## Portfolio Construction
  - Calculate the weight based on risk tolerance, expected return based on Mean-Variance model.
## Graph Plotting
  - Given the stock ticker and plot the trend of selected stock in different time windows.
## UI design
  - (to do)
