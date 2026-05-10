#Find Duplicate Characters

text = input("Enter a string: ")

seen = []
duplicates = []

for ch in text:
    if ch in seen:
        if ch not in duplicates:
            duplicates.append(ch)
    else:
        seen.append(ch)

print("Duplicate Characters:", duplicates)

'''
output:-

Enter a string: programming
Duplicate Characters: ['r', 'g', 'm']
'''