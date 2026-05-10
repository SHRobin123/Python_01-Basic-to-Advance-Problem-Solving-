#Count Words

text = input("Enter a sentence: ")

count = 1   # minimum 1 word ধরা হচ্ছে

for ch in text:
    if ch == " ":
        count += 1

print("Total Words:", count)

'''
output:-

Enter a sentence: I love Python
Total Words: 3
'''