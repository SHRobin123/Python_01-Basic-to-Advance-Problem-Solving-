#Replace Character

text = input("Enter a string: ")
old_char = input("Which character to replace: ")
new_char = input("Replace with: ")

result = ""

for ch in text:
    if ch == old_char:
        result += new_char
    else:
        result += ch

print("Updated String:", result)

'''
output:-

Enter a string: hello world
Which character to replace: l
Replace with: x
Updated String: hexxo worxd
'''