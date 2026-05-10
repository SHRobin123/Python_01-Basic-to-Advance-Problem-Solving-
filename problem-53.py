#Frequency of Characters
s = input("Enter string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")

for key in freq:
    print(key, "→", freq[key])

'''
output:-

Enter string: aabbbc
Character Frequency:
a → 2
b → 3
c → 1
'''