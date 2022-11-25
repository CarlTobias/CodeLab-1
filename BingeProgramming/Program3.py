# Program 3
print("\nWelcome to the Number Checker!\n")

num = int(input("Input a number: "))

if num == 0:
    print("This number is undefined.")

elif num > 0:
    print("This number is positive.")

else:
    print("This number is negative.")

again = input("\nWould you like to convert again? ").upper()

while True:
    if again == "YES" or again == "Y":
        num = int(input("Input a number: "))

        if num == 0:
            print("This number is undefined.")

        elif num > 0:
            print("This number is positive.")

        else:
            print("This number is negative.")

    else:
        print("Thank you! See you soon.")
        break