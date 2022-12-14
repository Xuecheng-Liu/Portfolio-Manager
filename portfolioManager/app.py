"""
This file will fire a flask app over local port
"""
from flask import Flask, render_template, request
from factorScore import get_sector_factor_table, get_sector_stock
from meanVariance import calculate_weight
from backTest import backtest
import time

app = Flask(__name__)



@app.route("/")
def home():
    '''
    end point for the main page
    '''
    return render_template("home.html")


@app.route("/new")
def new():
    '''
    end point for the sector forecasting
    '''
    return render_template("new.html")


# endpoint for experienced investor
@app.route("/old", methods=["GET", "POST"])
def old():
    '''
    end point for the sector forecasting with user input
    '''
    return render_template("old.html")


@app.route("/final", methods=["GET", "POST"])
def final():
    '''
    end point for portfolio page
    '''
    # get sectors selected from form
    sectors = request.form.getlist("sector")

    # get stock recommendations based on the sectors and number of stock per sector
    stock_list = get_sector_stock(int(request.form.get("num")), sectors)
    print(stock_list)

    # do the mean variance based on return,num and sectors
    mappings = calculate_weight(stock_list, float((request.form.get("return"))))
    ticker_list = []
    weight_list = []
    for key, value in mappings.items():
        ticker_list.append(key)
        weight_list.append(value)
    #backtest(ticker_list, weight_list)
    return render_template("final.html", sectors=sectors, mappings=mappings)


if __name__ == "__main__":
    app.run()
