# Most Frequent Character

text = input("Enter a string: ")

freq = {}

for char in text:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1

max_char = ""
max_count = 0

for char in freq:
    if freq[char] > max_count:
        max_count = freq[char]
        max_char = char

print("Most frequent character:", max_char)
print("Count:", max_count)

'''
output:-

Enter a string: aabbbcc
Most frequent character: b
Count: 3
'''