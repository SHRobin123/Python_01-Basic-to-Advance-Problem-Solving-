#Check Palindrome String

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse   # reverse বানানো হচ্ছে

if text == reverse:
    print("Palindrome String")
else:
    print("Not Palindrome")

'''
output:-

Enter a string: madam
Palindrome String
'''