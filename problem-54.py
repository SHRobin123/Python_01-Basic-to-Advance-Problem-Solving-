#Find First Non-Repeated Char
s = input("Enter string: ")

freq = {}

# Step 1: frequency count
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: find first unique
result = None

for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print("First Non-Repeated Character:", result)

'''
output:-

Enter string: aabbcde
First Non-Repeated Character: c
'''