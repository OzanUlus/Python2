from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

result = obj
result = type(obj)
result = type(html)
result = obj.prettify()
result = obj.title
result = type(obj.title)
result = obj.title.string

result = obj.body
result = obj.body.h1
result = obj.body.h1.string
result = obj.h1.string

result = obj.div
result = obj.h2
result = obj.ul
result = obj.ul.li










print(result)
