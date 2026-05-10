#String Compression
s = input("Enter string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

# last character add
result += s[-1] + str(count)

print("Compressed String:", result)

'''
output:-

Enter string: aaaabb
Compressed String: a4b2
'''