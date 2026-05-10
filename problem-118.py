#Group Anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    sorted_word = "".join(sorted(word))
    
    if sorted_word in groups:
        groups[sorted_word].append(word)
    else:
        groups[sorted_word] = [word]

print("Grouped Anagrams:", groups)

'''
output:-

Grouped Anagrams: {
    'aet': ['eat', 'tea', 'ate'],
    'ant': ['tan', 'nat'],
    'abt': ['bat']
}
'''