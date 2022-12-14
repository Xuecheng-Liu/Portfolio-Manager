from flask import Flask, render_template, request
from XGboost import xgb_model
from visualization import plot
from factorScore import get_sector_factor_table, get_sector_stock
from meanVariance import calculate_weight

app = Flask(__name__)



# end point for the main page
@app.route("/")
def home():
    return render_template("home.html")


# endpoint for new investor
@app.route("/new")
def new():
    return render_template("new.html")


# endpoint for experienced investor
@app.route("/old", methods=["GET", "POST"])
def old():
    # if request.method == "POST":
    #     print(request.form.getlist("sector"))
    return render_template("old.html")


@app.route("/final", methods=["GET", "POST"])
def final():
    # get sectors selected from form
    sectors = request.form.getlist("sector")

    # get stock recommendations based on the sectors and number of stock per sector


    stock_list = get_sector_stock(int(request.form.get("num")), sectors)
    print(stock_list)

    #stock_list = ['DOW', 'APD', 'VZ', 'T']
    # print((request.form.get("return")))
    # print(request.form.get("num"))
    # do the mean variance based on return,num and sectors
    mappings = calculate_weight(stock_list, float((request.form.get("return"))))
    print(mappings)
    return render_template("final.html", sectors=sectors,mappings=mappings)


if __name__ == "__main__":
    # for ticker in ticker_list:
    #     plot(xgb_model(ticker))
    app.run()
