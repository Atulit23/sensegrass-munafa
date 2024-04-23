import requests

response = requests.get("https://api.data.gov.in/catalog/859fe05b-eba0-402d-b777-eccd064734fd?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json")

data = response.json()

str_ = ''

for i in data['records']:
    str_ = str_ + 'Commodity: ' + i['commodity'] + ' Variety: ' + i['variety'] + ' Max Price: ' + str(i['max_price'])  + ' Min Price: ' + str(i['min_price']) + '\n'

print(str_)