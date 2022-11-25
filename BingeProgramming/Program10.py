# Program 10

print("\nWelcome to Number Guesser!\n")

print("Info: I will be asking you to input three numbers. I will then guess which is the largest out of the three.\n")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

if (num1 >= num2) and (num1 >= num3):
    largest = num1

elif (num2 >= num1) and (num2 >= num3):
    largest = num2

else:
    largest = num3

print(f"The largest number you inputted is {largest}.")