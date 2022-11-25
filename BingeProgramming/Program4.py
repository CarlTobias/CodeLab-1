# Program 4

print("\nWelcome to the Number Checker: optimusPRIME Edition!\n")

num = int(input("Input a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(str(num) + " is not a prime number.\n")
            break

        else:
            print(str(num) + " is a prime number.\n")

else:
    print(str(num) + " is not a prime number.\n")