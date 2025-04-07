import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
result = response
result = type(response)
result = response.status_code
result = response.headers
result = response.headers["Content-Type"]
result = response.url
result = response.text
posts = json.loads(response.text)
result = posts
result = posts[0]["title"]

for item in posts:
    if item["userId"] == 1:
        print(item["title"])




print(result)