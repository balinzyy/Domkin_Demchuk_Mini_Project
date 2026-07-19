import pandas as pd
import yfinance as yf

lockhead = "LMT"

raw_data = yf.download("LMT", period="3y")
filtered_data = raw_data[["Open", "Close", "Low", "High", "Volume"]]
cleaned_data = filtered_data.dropna()
print(cleaned_data)
