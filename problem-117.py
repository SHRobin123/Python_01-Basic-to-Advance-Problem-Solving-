#Word Frequency Counter

sentence = "I love python and I love coding"

words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:", freq)

'''
output:-

Word Frequency: {'I': 2, 'love': 2, 'python': 1, 'and': 1, 'coding': 1}
'''