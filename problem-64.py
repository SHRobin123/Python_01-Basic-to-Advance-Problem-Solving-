# Caesar Cipher

text = input("Enter text: ")
shift = 3

result = ""

for char in text:
    if char.isalpha():

        # uppercase letter
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # lowercase letter
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)

    else:
        result += char

print("Encrypted text:", result)

'''
output:-

Enter text: HELLO
Encrypted text: KHOOR
'''