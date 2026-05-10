# Count Words in File

# Create file with text
file = open("words.txt", "w")
file.write("Hello Python Programming Language")
file.close()

# Read file and count words
file = open("words.txt", "r")
content = file.read()

words = content.split()   # split by space
count = len(words)

print("File Content:")
print(content)
print("Total Words:", count)

file.close()

'''
output:-

File Content:
Hello Python Programming Language
Total Words: 4
'''