#Generator Function
def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)

'''
output:- 

1
2
3
'''