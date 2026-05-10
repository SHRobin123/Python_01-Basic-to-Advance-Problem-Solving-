#Invert Dictionary

student = {
    "name": "Robin",
    "age": 22,
    "department": "CSE"
}

inverted = {}

for key, value in student.items():
    inverted[value] = key

print("Inverted Dictionary:", inverted)

'''
output:-

Inverted Dictionary: {'Robin': 'name', 22: 'age', 'CSE': 'department'}
'''