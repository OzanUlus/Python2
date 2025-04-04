
numbers = [1,53,4,5,65,23]

result = sorted(numbers)
result = sorted(numbers,reverse=True)

users = [
    {"username" : "ozanulus", "posts" : ["post1","post2"], "email" : "info@ozan.com","phone" : "1234567890"},
    {"username" : "yusufbedlek", "posts" : [], "email" : "info@yusuf.com"},
    {"username" : "serhadmuhtar", "posts" : ["post1","post2","post3"],},
]
result = sorted(users , key=len)
result = sorted(users , key=lambda user : user["username"])
result = sorted(users , key=lambda user : len(user["posts"]))
result = sorted(users , key=lambda user : len(user["posts"]),reverse=True)




print(result)