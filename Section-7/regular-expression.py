import re

text = "Ozan Ulus Python Dersleri Ozan"
pattern = "Ozan"
match = re.search(pattern,text)
result = match
result = match.start()
result = match.end()

match = re.findall(pattern,text)
result = match


print(result)