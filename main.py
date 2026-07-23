import numpy as np
from datafile import cleaned_data


def trade(balance):
    amount = balance/cleaned_data.iloc[0]["Close"]
    for i in range(cleaned_data.shape[0]):
        if cleaned_data.iloc[i]["Signal"] == "Buy":
            amount = balance/cleaned_data.iloc[i]["Close"]
        elif cleaned_data.iloc[i]["Signal"] == "Sell":
            balance = amount*cleaned_data.iloc[i]["Close"]
            amount = 0

    if amount > 0:
        final_balance = amount*cleaned_data.iloc[-1]["Close"]
    else:
        final_balance = balance

    return final_balance

cleaned_data['FastMA'] = cleaned_data['Close'].rolling(window=20).mean()
cleaned_data['SlowMA'] = cleaned_data['Close'].rolling(window=100).mean()
cleaned_data['VolumeMA'] = cleaned_data['Volume'].rolling(window=20).mean()

cleaned_data.columns = cleaned_data.columns.get_level_values(0)
cleaned_data = cleaned_data.dropna()


today_signal = cleaned_data['FastMA'] > cleaned_data['SlowMA']
yesterday_signal = cleaned_data['FastMA'].shift(1) <= cleaned_data['SlowMA'].shift(1)

conds = [(today_signal & yesterday_signal), (~today_signal & ~yesterday_signal)]
signals = ["Buy", "Sell"]

cleaned_data["Signal"] = np.select(conds, signals, default="---")



summ = int(input("How much money do you want to invest?: "))
print(f"Balance after the selected period is {trade(summ):.2f}$. \nYour {"profit is" if trade(summ)-summ > 0 else "losses are"} {(trade(summ)-summ):.2f}$" )

