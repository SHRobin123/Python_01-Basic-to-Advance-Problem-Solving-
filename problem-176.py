# CSV File Reader

import csv

# Create a CSV file
file = open("data.csv", "w")
file.write("Name,Age,City\n")
file.write("Rahim,20,Dhaka\n")
file.write("Karim,22,Sylhet\n")
file.write("Sabbir,21,Kishoreganj\n")
file.close()

# Read CSV file
file = open("data.csv", "r")

reader = csv.reader(file)

print("CSV File Content:")

for row in reader:
    print(row)

file.close()

'''
output:-

CSV File Content:
['Name', 'Age', 'City']
['Rahim', '20', 'Dhaka']
['Karim', '22', 'Sylhet']
['Sabbir', '21', 'Kishoreganj']
'''