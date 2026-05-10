#Find Common Keys

dict1 = {
    "name": "Robin",
    "age": 22,
    "department": "CSE"
}

dict2 = {
    "age": 22,
    "department": "EEE",
    "university": "SUST"
}

common_keys = dict1.keys() & dict2.keys()

print("Common Keys:", common_keys)

'''
output:-

Common Keys: {'age', 'department'}
'''