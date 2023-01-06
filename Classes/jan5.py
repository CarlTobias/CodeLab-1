# revision of previous lectures


# task 1: write a program to create a function which returns the square root of a number
# call the funtion to print square root of consecutive 10 numbers

print("\nTask 1: ")
def squareroot(num):
    return (num ** (1/2))
  
for i in range(1,11):
    result = squareroot(i)
    print(f"The square root of {i} is: {result}.")


# task 2: what are the functions of lstrip, rstrip, and strip?
# write codes to use the funtions above

print("\nTask 2: ")
rndmtxt = " bananarama  "

# lstrip removes the empty text space on the left;
x = rndmtxt.lstrip()
print(f"This: {x}, is a random text.")

# rstrip removes the empty text space on the right;
y = rndmtxt.rstrip()
print(f"This: {y}, is a random text.")

# and strip removes the empty text space on both sides
z = rndmtxt.strip()
print(f"This: {z}, is a random text.")


# task 3: write a python program to check whether an alphabet is a vowel or consonant

print("\nTask 3: ")
vORc = input("Enter a letter in the alphabet: ").upper()

if vORc == "A" or vORc == "E" or vORc == "I" or vORc == "O" or vORc == "U":
    print(f"'{vORc}' is a vowel.")

else:
    print(f"'{vORc}' is a consonant.")


# task 4: take two numbers from user, compare and print the smaller number
# also consider a condition where both the numbers can be the same

print("\nTask 4: ")
num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))

if num1 > num2:
    print(f"{num2} is the smaller number.")

elif num1 < num2:
    print(f"{num1} is the smaller number.")

else:
    print(f"They are equal.")


# task 5: write a program to print all the elements in a list data type using for loop

print("\nTask 5: ")
litty = [1, 2, 3, 4, 5]

for items in litty:
    print(items)


# task 6: create a dictionary data-type of a student with name, id and course
# write a program to print all the key-value pair in the dictionary
# add another key-value pair called gender to update the dictionary and print the updated dictionary

print("\nTask 6: ")

personal_info = {"First Name": input("First Name: ").title(),
                "Last Name": input("Last Name: ").title(),
                "ID Number": input("ID Number: "),
                "Course": input("Course: ").upper()}

print("\n")
for key, value in personal_info.items():
    print(f"{key}: {value}")

print("\n")
personal_info["Gender"] = input("Gender: ").title()

print("\n")
for key, value in personal_info.items():
    print(f"{key}: {value}")


# task 7: declare 2 tuples comprising of 4 leap years and 4 non leap years

print("\nTask 7: ")
leapyrs = (2032, 2020, 2028, 2024)
nleapyrs = (2021, 2003, 2015, 2030)

# print tuples
print(leapyrs)
print(nleapyrs)
print("\n")

# concatenate 2 tuples
print(leapyrs + nleapyrs)
print("\n")

# multiple each tuple 3 times
print(leapyrs * 3)
print(nleapyrs * 3)
print("\n")

# compare 2 tuples
print(leapyrs == nleapyrs)
print("\n")

# find the length of tuples
print(len(leapyrs))
print(len(nleapyrs))
print("\n")

# find the sum of elements in each of the tuples
print(sum(leapyrs))
print(sum(nleapyrs))
print("\n")

# # sort the elements in each of the tuples
print(sorted(leapyrs))
print(sorted(nleapyrs))
print("\n")

# swap the tuples
leapyrs, nleapyrs = nleapyrs, leapyrs
print(f"The tuple with leap years now: {nleapyrs}")
print(f"The tuple with non-leap years now: {leapyrs}")
print("\n")


# task 8: write a program to print a number pattern

print("\nTask 8: ")
n = int(input("How many rows do you want? "))
i = 1

while i<=n:
    j=1
    while j<=i:
        print((i*2-1), end = " ")
        j += 1
    i += 1
    
    print()


# task 9: write a program to count the number of occurrence of a character in string

print("\nTask 9: ")
count = 0

word = "bananarama"
char = "a"

for i in word:
    if i == char:
        count += 1

print(f"The number of {char} in {word} is: {count}")


# task 10: write a program to create and print zero, one, two and multi-dimensional array importing NumPy module as array function

print("\nTask 10: ")
import numpy as np

arrayofvalues0 = np.array([120])
print(arrayofvalues0)
arrayofvalues1 = np.array([12, 4.25, 97, 80, 23.33, 67.67, 120])
print(arrayofvalues1)
arrayofvalues2 = np.array([[12, 4.25, 97, 80, 23.33, 67.67, 120], [12, 4.25, 97, 80, 23.33, 67.67, 120]])
print(arrayofvalues2)
arrayofvaluesmulti = np.array([[[12, 4.25, 97, 80, 23.33, 67.67, 120], [12, 4.25, 97, 80, 23.33, 67.67, 120]], [[12, 4.25, 97, 80, 23.33, 67.67, 120], [12, 4.25, 97, 80, 23.33, 67.67, 120]]])
print(arrayofvaluesmulti)

# task 11: turtle
# (please go to colab)
print("\nTask 11: (go to colab)")

# task 12: write a program to sort array in descending order

print("\nTask 12: ") 
plorp = np.array([12, 4.25, 97, 80, 23.33, 67.67, 120])

for i in range(len(plorp)):
    for j in range(i + 1, len(plorp)):
        if plorp[i] < plorp[j]:
            plorp[i], plorp[j] = plorp[j], plorp[i]
print(plorp)
            