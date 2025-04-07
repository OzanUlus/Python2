
from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

result = obj.find(id = "item1")
result = obj.find(id = "header")
result = obj.find(class_ = "item")
result = obj.find_all(class_ = "item")[1]

result = obj.select("#header")
result = obj.select("#item1")
result = obj.select(".item")

result = obj.select_one(".item")
result = obj.select_one("#item1")

result = obj.div.attrs["id"]
result = obj.div.attrs["class"]

result = obj.ul.get_text(strip=True,separator="-")

# print(result)

for a in obj.find_all("a"):
    print(a.get("href"))