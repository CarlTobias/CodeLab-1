# session 14 exercises

# program 1: write a program to find largest number and index position of the largest number in an array

import numpy as nnpp

arrayofvalues = nnpp.array([12, 4.25, 97, 80, 23.33, 67.67, 120])

orary = arrayofvalues[0]
index = 0

for i in range(1, len(arrayofvalues)):
    if orary < arrayofvalues[i]:
        orary = arrayofvalues[i]
        index = i
        
print(f"The highest number is {orary}")
print(f"The index is {index}")


# program 2: write a program to print array elements present on even positions

arrayofvalues = nnpp.array([12, 4.25, 97, 80, 23.33, 67.67, 120])

a = 0

while a < len(arrayofvalues):
    print(arrayofvalues[i], end = " ")
    a += 2


# program 3: write a program to print array elements present on odd positions

arrayofvalues = nnpp.array([12, 4.25, 97, 80, 23.33, 67.67, 120])

b = 1

while b < len(arrayofvalues):
    print(arrayofvalues[i], end = " ")
    b += 2


# program 4: write a program to sort array in descending order

arrayofvalues = nnpp.array([12, 4.25, 97, 80, 23.33, 67.67, 120])

print(f"Original Array: {arrayofvalues}")

length = len(arrayofvalues)

for i in range(length):
    for j in range(i + 1, length):
        if arrayofvalues[i] < arrayofvalues[j]:
            temp = arrayofvalues[i]
            arrayofvalues[i] = arrayofvalues[j]
            arrayofvalues[j] = temp
            
