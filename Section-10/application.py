import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "c66fdb442aa34fdb905100223250704"

lacation = input("Konum: ")

response = requests.get(url,params={
    "key": key,
    "q": lacation
})

result = response.json()
city = result["location"]["name"]
weather = result["current"]["temp_c"]

text = result["current"]["condition"]["text"]
print(weather)

print(f"{city} şu anda {weather} derece ve {text}")
