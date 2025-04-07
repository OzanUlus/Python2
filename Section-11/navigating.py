from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

result = obj.body.div.contents[3]

# for i in obj.body.div.children:
#     print(i)

# for i in obj.body.div.descendants:
#     print(i)

result = obj.body.h2.parent
result = obj.body.h2.parent.parent

result = obj.body.ul.next_element.next_element

result = obj.body.div.next_sibling.next_sibling
result = obj.body.div.find_next_sibling("div").find_next_sibling("div").find_previous_sibling("div")

print(result)