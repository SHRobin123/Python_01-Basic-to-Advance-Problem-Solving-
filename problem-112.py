#Merge Dictionaries

dict1 = {
    "name": "Robin",
    "age": 22
}

dict2 = {
    "department": "CSE",
    "university": "SUST"
}

merged = {**dict1, **dict2}

print("Merged Dictionary:", merged)

'''
output:-

Merged Dictionary: {'name': 'Robin', 'age': 22, 'department': 'CSE', 'university': 'SUST'}
'''