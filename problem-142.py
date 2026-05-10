#Decorator Function
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def hello():
    print("Hello!")

hello()

'''
output:- 

Before function
Hello!
After function
'''