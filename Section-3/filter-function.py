numbers = [1,3,5,-4,-2]

result = list(filter(lambda x : x < 0, numbers))
result = list(filter(lambda x : x % 2 == 0 , numbers))

names = ["çınar","ahmet","ada","yiğit","sena"]
result2 = list(filter(lambda x : x[0] == 'a',names))
result = list(map(lambda x : x.upper(),result2))




users = [
    {"username" : "ozanulus", "posts" : ["post1","post2"]},
    {"username" : "yusufbedlek", "posts" : []},
    {"username" : "serhadmuhtar", "posts" : ["post1","post2","post3"]},
]

result = list(filter(lambda user : len(user["posts"] ) > 0, users))
result = list(map(lambda u : u["username"],filter(lambda user : len(user["posts"] ) > 0, users)))
result = [user["username"].upper() for user in users if len(user["posts"]) > 0]
print(result)