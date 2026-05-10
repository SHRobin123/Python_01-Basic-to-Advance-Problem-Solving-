# Remove Punctuation

text = input("Enter a sentence: ")

punctuations = ".,!?;:'\"()-[]{}"

result = ""

for char in text:
    if char not in punctuations:
        result += char

print("After removing punctuation:", result)

'''
output:-

Enter a sentence: Hello, World! How are you?
After removing punctuation: Hello World How are you
'''