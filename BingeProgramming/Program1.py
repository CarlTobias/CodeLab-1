# Program 1

print("\n")
print("===============" * 6)
print("\nWelcome to the Conversion Program!\n")
choice = input("\nWould you like to convert your distance to kilometers or miles? ").upper()

if choice == "KILOMETERS" or choice == "KM":
    km = input("\n\nWhat is the distance (in kilometer) you'd like to convert? ")
        
    convert = float(km) * 0.62137

    print("\nYour converted distance is " + str(convert) + " km.")
    print("\nThank you for your conversion!")

elif choice == "MILES" or choice == "MI":
    mi = input("\n\nWhat is the distance (in miles) you'd like to convert? ")

    convert = float(mi) * 1.609

    print("\nYour converted distance is " + str(convert) + " mi.")
    print("\nThank you for your conversion!")

else:
    print("\nInvalid input. Please try again.")

again = input("\nWould you like to convert again? ").upper()

while True:
    if again == "YES" or again == "Y":
        if choice == "KILOMETERS" or choice == "KM":
            km = input(
                "\n\nWhat is the distance (in kilometer) you'd like to convert? ")

            convert = float(km) * 0.62137

            print("\nYour converted distance is " + str(convert) + " km.")
            print("\nThank you for your conversion!")

        elif choice == "MILES" or choice == "MI":
            mi = input("\n\nWhat is the distance (in miles) you'd like to convert? ")

            convert = float(mi) * 1.609

            print("\nYour converted distance is " + str(convert) + " mi.")
            print("\nThank you for your conversion!")

        else:
            print("\nInvalid input. Please try again.")
            break
    
    else:
        print("\nOkay. Thank you for your conversion!")
        print("\n")
        print("===============" * 6)
        print("\n")