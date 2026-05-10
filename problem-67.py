# String Permutations

from itertools import permutations

text = input("Enter a string: ")

perms = permutations(text)

print("All permutations:")

for p in perms:
    print("".join(p))

'''
output:-

Enter a string: ABC
All permutations:
ABC
ACB
BAC
BCA
CAB
CBA
'''