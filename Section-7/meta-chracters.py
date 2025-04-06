import re

text = "A343A  ABC 123 XYZ 456 @&% 300 2 A343A   123456  1_2 abc"

# pattern = r"\d\d\d"
# pattern = r"\d+"
# pattern = r"\d*"
# pattern = r"\d{3}"
# pattern = r"\d{3,5}"
# pattern = r"\d{3,}"
# pattern = r"\d{,5}"
# pattern = r"\d.\d"
# pattern = r"[a-zA-z0-9]"
# pattern = r"\d|[a-z]"
# pattern = r"\d|[a-z]"
# pattern = r"\d\w\w\w"
pattern = r"^A\d\w\w\w"

matches = re.search(pattern,text)

matches = re.findall(pattern,text)

matches = re.finditer(pattern,text)

for i in matches:
    print(i.group())


result = matches


print(result)