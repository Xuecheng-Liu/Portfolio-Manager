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
## Data Source and Preparation
For sector forecasting, data visualization and factor score parts, we use yahoo finance API to access all historical stock data and company financial statements. The training data includes 11 datasets for different sectors. Each dataset records the historical market data of specified sector index, which provide precise exposure to companies in this sector. And each datasets has 6 features, which consists of Open, High, Low, Close, Adj Close, Volume covering all time period.

+ XLB: companies in the chemical, construction material, containers and packaging, metals and mining, and paper and forest products industries
+ XLC: companies from telecommunication services, media, entertainment and interactive media & services
+ XLE: companies in the oil, gas and consumable fuel, energy equipment and services industries
+ XLF: companies in the diversified financial services; insurance; banks; capital markets; mortgage real estate investment trusts (“REITs”); consumer finance; and thrifts and mortgage finance industries
+ XLI: companies in the following industries: aerospace and defense; industrial conglomerates; marine; transportation infrastructure; machinery; road and rail; air freight and logistics; commercial services and supplies; professional services; electrical equipment; construction and engineering; trading companies and distributors; airlines; and building products
+ XLK: companies from technology hardware, storage, and peripherals; software; communications equipment; semiconductors and semiconductor equipment; IT services; and electronic equipment, instruments and components
+ XLP: companies from the food and staples retailing, beverage, food product, tobacco, household product and personal product industries in the U.S
+ XLRE:  companies from real estate management and development and REITs, excluding mortgage REITs
+ XLU: companies from the electric utility, water utility, multi-utility, independent power and renewable electricity producers, and gas utility industries
+ XLV: companies in the pharmaceuticals; health care equipment and supplies; health care providers and services; biotechnology; life sciences tools and services; and health care technology industries
+ XLY: companies in retail (specialty, multiline, internet and direct marketing); hotels, restaurants and leisure; textiles, apparel and luxury goods; household durables; automobiles; auto components; distributors; leisure products; and diversified consumer services.

For XGBoost training, our model takes all 11 sectors historial price data from all time horizion.
For calculating factor and portfolio weight, our model fetches real-time stock infomaiton and company financial statement.
All financial data used in XGBoost trainning and portfolio calculating are all fetched from Yahooo Finance API.
## XGBoost and Feature Engineering
  - XGBoost (Extreme Gradient Boosting) is a popular supervised-learning algorithm used for regression and classification on large datasets.
    It uses sequentially-built shallow decision trees to provide accurate results and a highly-scalable training method that avoids overfitting.
  - We selected some basic but effective market features like EMA, SMA, momentum, K-line for feature trainning.
## Factor-Based Strategy
  We select 3 significant stock factors for our inner-sector selecting process. This is our application's basic stock selecting strategy.
  - Dividend Rate: Dividend shows how much a company pay out each year relative to its stock price. It is an important indicator of stock pricing.
  - Operating Cash Flow / Market Capital: This indicates how much a company can pay for its operation relative to its total capital. It is an important indicator for company earnings.
  - Return On Equity / Price to Book: This indicates how much a stock is undervalued. It is an important fundamental signal for buying this stock
  All these 3 factors are effective ones on the stock market now, because it is statistically significant with stock price in recent months.
## Factor-Scoring Method:
  - All these 3 factors are positively correlated with stock return, so our scoring-method would assign higher score for those stocks that have larger factor value. Then we add scores together to screen out the best n stocks for each investor-selected sector.
## Mean-Variance Algorithm
  - This is a classic investment model for calculating portfolio weight based on Markowitz Optimization. Given a target return level, we can calculate the portfolio weight with minimum variance (risk).
## Visualization
  - We use matplotlib package for plotting our forecasting and back-testing graph. It is a handy and readable way to visualize our prediction.
## UI design
  - Integerated HTML, CSS and Bootstrap with Flask framework to generate web page, user interactive session and communicate data with back end.
