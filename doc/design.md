# User 1
X1 is interesed in the stock market and would like to see the trend of a particular stock.
- use case: user enter the stock symbol in the search bar and we display some general information about that stock in different time horizons

# User2
X2 would like to know which secters in the market has a promising trend in the next few days.
-  use case: user will be exposed to the forecasting of different sectors in rank for the next few days

# User3
X3 with moderate knowledge in investing and would like to know which stocks to buy in the next few days to make profit.
- use case: user will be exposed to the recommended stocks from different sectors in rank.

# User4
X4 with experienced investing experience and would like to know the portfolio setup with a particular risk tolerance and expected return for a fixed amout the stock selections.
- user case: user will enter a risk tolerance, expected return and number of stocks. we provide the weight for each stock in the portfolio.




# Component
- data fetching
  fetch the market data from Yahoo Finance and store it in the csv files
- feature engineering
  process the raw data and add artificial features based on raw data for later training
- model setup
  use tensor flow to initilize the LSTM model
- hyperparameter tuning
  find the best number of hidden layer, number of neurons per layer and drop rate for the model
- prediction function
  use data fetching component to get the target input data and output the predicted return of stocks
- factor selction and calculation
  select a particular factor and output the score of a particular stock
- stock ranking
  rank the stocks within a particular sector based on factor selection and calculation
- portfolio construction
  calculate the weight based on risk tolerance, expected return and target stocks.
- trend plotting
  given the stock symbol and plot the trend of that stock in different time horizons
- UI design
  (to do)
