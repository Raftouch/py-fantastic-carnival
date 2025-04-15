import requests
import time

response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})

# content = response.content
# print(content)
# print(type(content)) # <class 'bytes'>

# price_dict = response.json()
# price = float(price_dict['price'])
# print(price)

bitcoint_prices = []
for i in range(30):
    price = float(response.json()['price'])
    bitcoint_prices.append(price)
    time.sleep(1)

print(bitcoint_prices)
print(len(bitcoint_prices))
print(max(bitcoint_prices))
print(min(bitcoint_prices))

