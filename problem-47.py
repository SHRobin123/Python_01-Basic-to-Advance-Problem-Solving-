#Remove Spaces

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("Without Spaces:", result)

'''
output:-

Enter a string: I love Python
Without Spaces: IlovePython
'''