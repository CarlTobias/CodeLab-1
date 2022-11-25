# Program 2

print("\n")
print("===============" * 6)
print("\nWelcome to the Conversion Program: Temperature Edition!\n")




choice = input("\nWould you like to convert your temperature to celsius or fahrenheit? ").upper()

if choice == "CELSUIS" or choice == "C":
    f = input("\n\nWhat is the temperature (in fahrenheit) you'd like to convert? ")

    convert = (float(f) - 32) * 0.5556

    print("\nYour converted temperature is " + str(convert) + " °C.")
    print("\nThank you for your conversion!")

elif choice == "FAHRENHEIT" or choice == "F":
    c = input("\n\nWhat is the temperature (in celsius) you'd like to convert? ")

    convert = (float(c) * 1.8) + 32

    print("\nYour converted distance is " + str(convert) + " °F.")
    print("\nThank you for your conversion!")

else:
    print("\nInvalid input. Please try again.")

again = input("\nWould you like to convert again? ").upper()

while True:
    if again == "YES" or again == "Y":
        if choice == "CELSUIS" or choice == "C":
            f = input("\n\nWhat is the temperature (in fahrenheit) you'd like to convert? ")

            convert = (float(f) - 32) * 0.5556

            print("\nYour converted temperature is " + str(convert) + " °C.")
            print("\nThank you for your conversion!")

        elif choice == "FAHRENHEIT" or choice == "F":
            c = input("\n\nWhat is the temperature (in celsius) you'd like to convert? ")

            convert = (float(c) * 1.8) + 32

            print("\nYour converted distance is " + str(convert) + " °F.")
            print("\nThank you for your conversion!")

        else:
            print("\nInvalid input. Please try again.")
    
    else:
        print("\nOkay. Thank you for your conversion!")
        print("\n")
        print("===============" * 6)
        print("\n")