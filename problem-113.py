#Sort Dictionary

student = {
    "name": "Robin",
    "age": 22,
    "department": "CSE",
    "grade": "A"
}

sorted_dict = dict(sorted(student.items()))

print("Sorted Dictionary:", sorted_dict)

'''
output:-

Sorted Dictionary: {'age': 22, 'department': 'CSE', 'grade': 'A', 'name': 'Robin'}
'''