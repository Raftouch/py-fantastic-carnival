import requests

# response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'ETHUSDT'})

# # content = response.content
# # print(content)

# price = float(response.json()['price'])
# print(price)


response = requests.get('https://api.binance.com/api/v3/ticker/price')

res = response.json()
for r in res:
    if r["symbol"] == 'ETHUSDT':
        print(float(r['price']))