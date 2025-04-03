
result = [i for i in range(1,101) if i % 12 == 0]
print(result)

print("-----------------------------------------------------")

text = "Hello 12345 World"
numbers = [num  for num in text if num.isdigit()]
print(numbers) 

print("-----------------------------------------------------")

temperatures = [20, 15, 0, -5, -2]
notification = [temperature if temperature > 4 else "risk of icing" for temperature in temperatures]
print(notification) 

print("-----------------------------------------------------")

students = ["ali", "ahmet", "candan"]
scores = [50, 60, 80]

highScores = {students[i] : scores[i] for i in range(len(students)) if scores[i] > 50 }
print(highScores) 

print("-----------------------------------------------------")

result2 = [(x, y) for x in range(3) for y in range(3)]
print(result2) 

print("-----------------------------------------------------")




