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
- Step 4: Generate sectors forecasting with `python train.py` <br>
- Step 5: Initialize our application with `python portfolioManager.py` <br>
- Step 6: Copy the URL link `http://127.0.0.1:5000` to your favourite browser and begin your investment adventure!

## Testing
Enter the commend `python -m unittest` at the top-level directory `Portfolio-Manager`.

## Acknowledgement
Many thanks to Dr. David Beck and Elizabeth Pelletier from the University of Washington for their support, guidance, and feedback in the development of this project.
