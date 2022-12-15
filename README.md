# Portfolio-Manager
**Team Members**: Xuecheng Liu, Wei Liu, Shengbo Jin, Patrick Xiao

## Project Objective
Help our investors with getting forecasting on sectors and give investment advice on constructing a stock portfolio from their preferred sectors based on sector forecasting and factor-selecting strategy.

## Repository Structure
 ```
.
├── data
├── doc
├── portfolioManager
├── statelegiscraper
│   ├── XGboost
│   ├── backTest
│   ├── factorScore
|   ├── meanVariance
|   ├── static
|   ├── templates
|   ├── visualization
|   ├── app.py
|   ├── train.py
│   └── test
├── LICENSE
├── README.md
└── environment.yml
 ```

## Usage
Enter the following commends into the terminal <br>
- Step 1: git clone our repoistory with `git clone git@github.com:Xuecheng-Liu/Portfolio-Manager.git`<br>
- Step 2: install the virtual env using `conda env create -f environment.yml` <br>
- Step 3: change your current directory with `cd portfolioManager` <br>
- Step 4: generate sectors forecasting with `python train.py` <br>
- Step 5: initialize our application with `python portfolioManager.py` <br>
- Step 6: copy the URL link `http://127.0.0.1:5000` to your favourite browser and begin your investment adventure! <br>

## Future Work
Considering the user experience while using the web app, we only select the top 10 component stocks in each sector to reducing the waiting time while using the app. Future work to address this issue might develop a database in the backend to keep tracking of component stocks instead of making real-time API call to Yahoo Finance.
Meanwhile, the website would crash (diplay internal server error) if the meanVariance module cannot find the solution based on user input.

## Testing
Run the commend `python -m unittest` at the top-level directory `Portfolio-Manager`.
All 9 tests should be run around 100 secs.

## Acknowledgement
Many thanks to Dr. David Beck and Elizabeth Pelletier from the University of Washington for their support, guidance, and feedback in the development of this project.
