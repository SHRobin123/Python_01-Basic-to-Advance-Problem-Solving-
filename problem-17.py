#Armstrong Number
num = int(input("Enter a number: "))

original = num

sum = 0

while num > 0:

    digit = num % 10

    sum = sum + digit ** 3

    num = num // 10

if original == sum:
    print("Armstrong Number")

else:
    print("Not Armstrong")


'''
output:-
Enter a number: 153

Armstrong Number

Enter a number: 123

Not Armstrong

Example → 153

1
3
+
5
3
+
3
3
=1+125+27=153

'''