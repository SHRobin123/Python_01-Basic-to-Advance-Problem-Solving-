# Write File

# Writing data into file (overwrite mode)
file = open("write_demo.txt", "w")
file.write("Hello Python\nThis is file writing example")
file.close()

# Reading file to show output
file = open("write_demo.txt", "r")
content = file.read()

print("File Content:")
print(content)

file.close()

'''
output:-

File Content:
Hello Python
This is file writing example
'''