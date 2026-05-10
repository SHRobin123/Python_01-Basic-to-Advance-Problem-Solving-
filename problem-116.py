#Nested Dictionary

students = {
    "student1": {
        "name": "Robin",
        "age": 22,
        "department": "CSE"
    },
    "student2": {
        "name": "Rahim",
        "age": 21,
        "department": "EEE"
    }
}

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Department:", students["student2"]["department"])

print("Full Dictionary:", students)

'''
output:-

Student 1 Name: Robin
Student 2 Department: EEE
Full Dictionary: {'student1': {'name': 'Robin', 'age': 22, 'department': 'CSE'}, 'student2': {'name': 'Rahim', 'age': 21, 'department': 'EEE'}}
'''