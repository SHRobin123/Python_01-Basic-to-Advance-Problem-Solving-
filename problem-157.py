#Static Method

class Math:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# object ছাড়াই call করা যায়
print("Addition:", Math.add(5, 3))
print("Multiplication:", Math.multiply(4, 6))

'''
output:-

Addition: 8
Multiplication: 24
'''