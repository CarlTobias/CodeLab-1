# Exercise 2:
# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free;

# if they are between 3 and 12, the ticket is $10
# and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

print("\nExercise 2\n")

# first, the program will welcome the user
print("Welcome to the Red Carpet Cinema!\n")

# i wanted to make it so that users could do bulk purchases,
# but my knowledge has not reached that level just yet,
# so we have to apologize for the inconvenience for now
print("As of now, our website can only process one purchase at a time.")
print("We are sorry for the inconvenience.\n")

# i assigned two variables right off the bat...
# first is the user input, and the second is just equal to zero
ticket = int(input("How many tickets would you like to buy? "))
times = 0

# and here, you can see why...
# whatever the user inputs, as long as "times" is not equal to it, the program will continue to run
while ticket != times:
    # here, i made this formula so that it will add one every time the program repeats 
    # (so that it will eventually equal to "tickets")
    times = times + 1
    # i told the program to ask for the user's age (and i defined it as an integer)
    age = int(input("\nHow old are you? "))
    
    # this if-else statement analyzes the age input
    # and it will print the following in the slot which fits the condition
    if age < 3:
        print("The ticket for this age is free! Enjoy the movie.\n")
    
    elif age >= 3 and age <= 12:
        print("At the moment, each individual ticket will be priced at €10.\n")
    
    elif age >= 12:
        print("At the moment, each individual ticket will be priced at €15.\n")
    
    elif age >= 62:
        print("At the moment, each individual ticket will be priced at €7.\n")

# finally, the program thanks the user before ending the program
print("Thank you for visting our site! See you soon.\n")