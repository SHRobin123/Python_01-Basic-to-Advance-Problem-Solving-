# JSON File Handling

import json

# Create data (dictionary format)
data = {
    "name": "Sabbir",
    "age": 21,
    "city": "Kishoreganj"
}

# Write JSON file
file = open("data.json", "w")
json.dump(data, file)
file.close()

# Read JSON file
file = open("data.json", "r")
loaded_data = json.load(file)

print("JSON File Content:")
print(loaded_data)

print("Name:", loaded_data["name"])
print("Age:", loaded_data["age"])

file.close()

'''
output:-

JSON File Content:
{'name': 'Sabbir', 'age': 21, 'city': 'Kishoreganj'}

Name: Sabbir
Age: 21
'''