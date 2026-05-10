# Append File

# First writing initial content
file = open("append_demo.txt", "w")
file.write("Hello Python\n")
file.close()

# Now appending new content
file = open("append_demo.txt", "a")
file.write("This is appended line\n")
file.write("Another new line added")
file.close()

# Reading file to show final output
file = open("append_demo.txt", "r")
content = file.read()

print("File Content:")
print(content)

file.close()

'''
output:-

File Content:
Hello Python
This is appended line
Another new line added
'''