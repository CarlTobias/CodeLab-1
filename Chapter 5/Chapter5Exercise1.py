print("\nExercise 1\n")

personal_info = {"First Name": input("First Name: "),
                "Last Name": input("Last Name: "),
                "Age": input("Age: "),
                "City": input("City: "),
                "Country": input("Country: ")}

print("First Name: " + personal_info["First Name"])
print("Last Name: " + personal_info["Last Name"])
print("Age: " + personal_info["Age"])
print("City: " + personal_info["City"])

yno = input("\nIs this information correct? ").upper()

if yno == "YES":
    print("Data is saved. Thank you for your cooperation.")

elif yno == "NO":
    print("Please try again.\n")

    personal_info = {"First Name": input("First Name: "),
                     "Last Name": input("Last Name: "),
                     "Age": input("Age: "),
                     "City": input("City: "),
                     "Country": input("Country: ")}

    print("First Name: " + personal_info["First Name"])
    print("Last Name: " + personal_info["Last Name"])
    print("Age: " + personal_info["Age"])
    print("City: " + personal_info["City"])

    yno = input("\nIs this information correct? ").upper()

    if yno == "YES":
        print("Data is saved. Thank you for your cooperation.\n")
    
    else:
        print("Error. Please reset the program and try again\n.")

else:
    print("Error. Reset the program.\n")
