# Copy File

# Create original file
file = open("original.txt", "w")
file.write("Hello Python\nThis is original file content")
file.close()

# Read from original file
file = open("original.txt", "r")
content = file.read()
file.close()

# Write into new file (copy)
file = open("copy.txt", "w")
file.write(content)
file.close()

# Read copied file
file = open("copy.txt", "r")
copied_content = file.read()

print("Copied File Content:")
print(copied_content)

'''
output:-

Copied File Content:
Hello Python
This is original file content
'''