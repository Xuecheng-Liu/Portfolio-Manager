from flask import Flask, render_template, request
from XGboost import xgb_model
from visualization import plot
app = Flask(__name__)

ticker_list = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]


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
    sectors = request.form.getlist("sector")
    print(sectors)
    print((request.form.get("return")))
    print(request.form.get("num"))
    # do the mean variance based on return,num and sectors
    f = open("test.txt", "r")
    print(f.read())
    return render_template("final.html", sectors=sectors)



if __name__ == "__main__":
    # for ticker in ticker_list:
    #     plot(xgb_model(ticker))
    app.run()