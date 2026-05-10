#Reverse Words

text = input("Enter a sentence: ")

words = text.split()   # sentence কে word এ ভাঙা

reverse = ""

for i in range(len(words)-1, -1, -1):
    reverse += words[i] + " "

print("Reversed Words:", reverse.strip())

'''
output:-

Enter a sentence: I love Python
Reversed Words: Python love I
'''