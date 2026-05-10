#Remove Duplicate Characters

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("Without Duplicates:", result)

'''
output:-

Enter a string: programming
Without Duplicates: progamin
'''