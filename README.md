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
step 1: git clone our repoistory with `git clone git@github.com:Xuecheng-Liu/Portfolio-Manager.git`<br>
step 2: install the virtual env using `conda env create -f environment.yml` <br>
step 3: change your current directory with `cd portfolioManager` <br>
step 4: Generate sectors forecasting with `python train.py` <br>
step 5: Initialize our application with `python app.py` <br>
step 6: Copy the URL link to your favourite browser and begin your investment adventure!

## Acknowledgement
Many thanks to Dr. David Beck and Elizabeth Pelletier from the University of Washington for their support, guidance, and feedback in the development of this project.
