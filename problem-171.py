# Read File

# Create a sample file first (for demo)
file = open("demo.txt", "w")
file.write("Hello Python\nWelcome to File Handling")
file.close()

# Now read the file
file = open("demo.txt", "r")
content = file.read()
print("File Content:")
print(content)
file.close()

'''
output:-

File Content:
Hello Python
Welcome to File Handling
'''