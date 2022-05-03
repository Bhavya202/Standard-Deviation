# Importing Modules
import math
import csv
import statistics

# List Of Elements To Calculate Mean
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

# Finding Mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

# Squaring And Getting The Values
squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

# Getting Sum
sum = 0
for i in squared_list:
    sum = sum + i

# Divinding The Sum By Total Values
result = sum / (len(data) - 1)

# Printing Some Text
print()
print("----------------------------------Standard Deviation----------------------------------")
print()

# Getting The Deviation By Taking Square Root Of The Result
std_deviation = math.sqrt(result)

print("Standard Deviation Using Formula:-")
print("Standard Deviation Is: " + str(std_deviation))
print()

# Getting Standard Deviation Using A Predefined Function
data = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96] # Data From 'data.csv' File
std_deviation = statistics.stdev(data)

print("Standard Deviation Using Predefined Function:-")
print("Standard Deviation Is: " + str(std_deviation))
print()