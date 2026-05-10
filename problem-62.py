# Find Longest Word

text = input("Enter a sentence: ")

words = text.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

'''
output:-

Enter a sentence: I love programming in Python
Longest word: programming
'''