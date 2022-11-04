# Exercise 1:
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

print("\nExercise 1\n")

# here i made a dictionary named "personal_info" that collects a user's personal information
# dictionaries contain key-value pairs...
# for my dictionary, i have keys that are string, and user input for value
# (using strings are also possible for "values")
personal_info = {"First Name": input("First Name: "),
                "Last Name": input("Last Name: "),
                "Age": input("Age: "),
                "City": input("City: "),
                "Country": input("Country: ")}

# the line of codes from line 20 until 23 prints the info that was inputted in the dictionary
print("First Name: " + personal_info["First Name"])
print("Last Name: " + personal_info["Last Name"])
print("Age: " + personal_info["Age"])
print("City: " + personal_info["City"])

# now here, i told the program to ask a yes or no question to the user...
# i would like to ask if the information is correct or not
yno = input("\nIs this information correct? ").upper()

# here is the if-else statement that checks if the user input matches the condition
if yno == "YES":
    # if yes, then the user will be informed that the data entered and is saved thanked
    # for their cooperation, then and the program is ended
    print("Data is saved. Thank you for your cooperation.")

elif yno == "NO":
    # if no, the user is asked to try again
    print("Please try again.\n")

    # the user will have to input once again
    personal_info = {"First Name": input("First Name: "),
                     "Last Name": input("Last Name: "),
                     "Age": input("Age: "),
                     "City": input("City: "),
                     "Country": input("Country: ")}

    print("First Name: " + personal_info["First Name"])
    print("Last Name: " + personal_info["Last Name"])
    print("Age: " + personal_info["Age"])
    print("City: " + personal_info["City"])

    # and the user is asked again if the information is right
    yno = input("\nIs this information correct? ").upper()

    # same if-else statement here
    if yno == "YES":
        print("Data is saved. Thank you for your cooperation.\n")
    
    else:
        # but if the user inputs anything other than "YES," then they will have to reset the program
        print("Please reset the program. Maximum attemps reached.\n.")

# this else statement is just in case (for the first try,)
# the user inputs anything other than "YES" or "NO"
else:
    print("Error. Reset the program.\n")
