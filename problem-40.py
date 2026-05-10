# Reverse a String

text = input("Enter a string: ")

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed string:", reversed_text)

'''
output:-

Enter a string: hello
Reversed string: olleh
'''