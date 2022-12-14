from XGboost import xgb_model
from visualization import plot

data = xgb_model("XLY")
plot(data)