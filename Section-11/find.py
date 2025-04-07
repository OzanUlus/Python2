from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

result = obj.div
result = obj.find("div")
result = obj.find_all("div")
result = len(obj.find_all("div"))
result = obj.find_all("div")[1].h2
result = obj.find_all("div")[1].ul
result = obj.find_all("div")[1].ul.li
result = obj.find_all("div")[1].ul.find_all("li")[2]
result = obj.find_all("div")[1].ul.find_all("li")[2].string

# print(result)

for div in obj.find_all("div"):
    if div.h2.a != None:
        print(div.h2.a.string.strip())
    else:
        print(div.h2.string.strip())

for a in obj.find_all("a"):
    print(a)