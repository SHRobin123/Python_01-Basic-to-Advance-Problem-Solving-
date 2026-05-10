# Count Vowels in String

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for ch in text.lower():
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

'''
output:-

Enter a string: Hello World
Number of vowels: 3
'''