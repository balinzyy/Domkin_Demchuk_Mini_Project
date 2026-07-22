from unittest import skip

import numpy as np
from datafile import cleaned_data
import matplotlib.pyplot as plt
import pandas as pd

cleaned_data['FastMA'] = cleaned_data['Close'].rolling(window=10).mean()
cleaned_data['SlowMA'] = cleaned_data['Close'].rolling(window=100).mean()
cleaned_data['VolumeMA'] = cleaned_data['Volume'].rolling(window=20).mean()

cleaned_data = cleaned_data.dropna()


today_signal = cleaned_data['FastMA'] > cleaned_data['SlowMA']
yesterday_signal = cleaned_data['FastMA'].shift(1) <= cleaned_data['SlowMA'].shift(1)

conds = [(today_signal & yesterday_signal), (~today_signal & ~yesterday_signal)]
signals = ["Buy", "Sell"]

cleaned_data["Signal"] = np.select(conds, signals, default="---")

#print(cleaned_data.to_string())
first_index = cleaned_data[cleaned_data["Signal"] == "---"].index[0]
cleaned_data.loc[first_index, "Signal"] = "Buy"
buy_sell_df = cleaned_data[cleaned_data["Signal"] != "---"]
print(buy_sell_df)

total_buy = cleaned_data[cleaned_data["Signal"]=="Buy"]["Close"].sum()


total_sell = cleaned_data[cleaned_data["Signal"]=="Sell"]["Close"].sum()

total_pnl = total_sell - total_buy
clean_pnl = total_pnl.item()
print(f"{clean_pnl:.2f} $")

