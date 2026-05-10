#Frozen Set Usage

numbers = {1, 2, 3, 4, 5}

fset = frozenset(numbers)

print("Frozen Set:", fset)

# Trying to modify (will cause error if uncommented)
# fset.add(6)

'''
output:-

Frozen Set: frozenset({1, 2, 3, 4, 5})
'''