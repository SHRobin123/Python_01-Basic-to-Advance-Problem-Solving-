#Capitalize First Letter

text = input("Enter a sentence: ")

words = text.split()

result = ""

for word in words:
    result += word.capitalize() + " "

print("Capitalized Sentence:", result.strip())

'''
output:-

Enter a sentence: i love python
Capitalized Sentence: I Love Python
'''