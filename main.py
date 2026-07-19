import numpy as np
from datafile import cleaned_data

cleaned_data['FastMA'] = cleaned_data['Close'].rolling(window=10).mean()
cleaned_data['SlowMA'] = cleaned_data['Close'].rolling(window=100).mean()
cleaned_data['VolumeMA'] = cleaned_data['Volume'].rolling(window=20).mean()

cleaned_data = cleaned_data.dropna()


today_signal = cleaned_data['FastMA'] > cleaned_data['SlowMA']
yesterday_signal = cleaned_data['FastMA'].shift(1) <= cleaned_data['SlowMA'].shift(1)

conds = [(today_signal & yesterday_signal), (~today_signal & ~yesterday_signal)]
signals = ["Buy", "Sell"]

cleaned_data["Signal"] = np.select(conds, signals, default="---")

print(cleaned_data.to_string())

