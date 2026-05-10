# Reverse Each Word

text = input("Enter a sentence: ")

words = text.split()

result = []

for word in words:
    result.append(word[::-1])

print("Reversed words sentence:", " ".join(result))

'''
output:-

Enter a sentence: I love Python
Reversed words sentence: I evol nohtyP
'''