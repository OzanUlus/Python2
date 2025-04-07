import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data={
    "userId": 1,
    "title": "Yeni gönderi",
    "body": "Yeni gönderi açıklaması"
})

result = response
result = response.text
result = response.json()
result = response.headers

print(result)