#Difference Between Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

diff = []

for i in list1:
    if i not in list2:
        diff.append(i)

for i in list2:
    if i not in list1:
        diff.append(i)

print("Difference:", diff)

'''
output:-

Difference: [1, 2, 5, 6]
'''