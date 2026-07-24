import matplotlib.pyplot as plt
from main import cleaned_data

plt.figure(figsize=(20, 10), dpi=200)

plt.plot(cleaned_data.index, cleaned_data['Close'], label='Ціна закриття (Close)', color='black')

plt.plot(cleaned_data.index, cleaned_data['FastMA'], label='Швидка MA (10 днів)', color='blue')
plt.plot(cleaned_data.index, cleaned_data['SlowMA'], label='Повільна MA (100 днів)', color='red')

buys = cleaned_data[cleaned_data['Signal'] == 'Buy']
sells = cleaned_data[cleaned_data['Signal'] == 'Sell']
plt.scatter(buys.index, buys['Close'], marker='^', color='green', s=150, label='Купівля (Buy)')
for date in buys.index:
    plt.axvline(x=date, color='green',linestyle='--')

plt.scatter(sells.index, sells['Close'], marker='v', color='red', s=150, label='Продаж (Sell)')
for date in sells.index:
    plt.axvline(x=date, color='red', linestyle='--')
plt.grid(True, which='major', color='black', linestyle=':', alpha=0.5)

plt.title("Торгова стратегія для Lockheed Martin (LMT)")
plt.xlabel("Дата")
plt.ylabel("Ціна ($)")

plt.show()