#Leap Year Check

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")

else:
    print(year, "is NOT a Leap Year")


    '''
 output:-
 Enter a year: 2024
2024 is a Leap Year

Enter a year: 2025
2025 is NOT a Leap Year
    '''