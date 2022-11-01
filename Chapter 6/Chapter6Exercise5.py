# Exercise 5:
# Using the list sandwich_orders from Exercise 7-8,
# make sure the sandwich 'pastrami' appears in the list at least three times.

# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.

# Make sure no pastrami sandwiches end up in finished_sandwiches.

from re import S


print("\nExercise 5\n")

# this exercise is basically just an iteration of the previous one,
# so i won't be explaining the whole thing again
# i'll be be explaining the new codes that i added to fit the description of the exercise

# firstly, i added new text that will inform the user that there is no pastrami in stock
print("Welcome to The New Deli!\n")
print("We are sorry to inform you that we have run out of pastrami. Sorry for the inconvenience.")
print("We will try our best to bring back our best seller as soon as possible.\n")

sandwichesamount = int(input("How many sandwiches would you like to order? "))
orders = 1

sandwich_orders = []
finished_sandwich = []

# inside this if-else statement is another if-else statement that takes into account
# the possibility that the user will input "Pastrami"
if sandwichesamount == 1:
    sandwichflavours = input("\nWhat flavour sandwich would you like? ").title()
    sandwich_orders.append(sandwichflavours)

    # so, if the user inputs "Pastrami," the following code will be executed
    orders2 = 0
    if sandwichflavours == "Pastrami":
        sandwich_orders.pop()
        # the program will print this message telling them to try again
        print("\nI'm sorry. We don't have any pastrami at the moment.")
        print("Please try again.\n")
        
        # this "while" loop enables the program to repeat until the user enters a valid sandwich flavour
        while sandwichesamount != orders2:
            orders2 = orders2 + 1
            sandwichflavours = input("\nWhat flavour sandwich would you like? ").title()
            sandwich_orders.append(sandwichflavours)

            # this if-else block scans for the string input...
            # if it equals to "Pastrami," the program will keep telling the user to try again
            if sandwichflavours == "Pastrami":
                sandwich_orders.append(sandwichflavours)
                sandwich_orders.pop()
                print("\nI'm sorry. We don't have any pastrami at the moment.")
                print("Please try again.\n")
                orders = orders - 1

            # if the user finally enters a valid input,
            # then the program will continue as per usual
            elif sandwichflavours != "Pastrami":
                while sandwich_orders:
                    current_sandwich = sandwich_orders.pop()
                    print("I made your " + current_sandwich.lower() + " sandwich.")
                    finished_sandwich.append(current_sandwich)

    # now this part will be executed only if, on the first try, the user inputs a valid sandwich flavour
    else:
        current_sandwich = sandwich_orders.pop()
        print("Okay! I made your " + current_sandwich.lower() + " sandwich.")
        finished_sandwich.append(current_sandwich)

        print("\n")
        print("Sandwich Orders: ")

        for sandwich in finished_sandwich:
            print(sandwich + " Sandwich")
        print("\n")

# this block is for the option where the user wants more than one sandwich
else:
    sandwichflavours = input("\nWhat flavour sandwich would you like? ").title()
    sandwich_orders.append(sandwichflavours)

    # so in this block, i repeated the code once again to prevent the bug where
    # they can order pastrami if that's the first thing that they input
    if sandwichflavours == "Pastrami":
        sandwich_orders.pop()
        print("\nI'm sorry. We don't have any pastrami at the moment.")
        print("Please try again.\n")
        orders = orders - 1

        while sandwichesamount != orders:
            orders = orders + 1
            sandwichflavours = input("\nWhat other flavour sandwich would you like? ").title()
            sandwich_orders.append(sandwichflavours)

            current_sandwich = sandwich_orders.pop()
            print("Okay! I made your " + current_sandwich.lower() + " sandwich.")
            finished_sandwich.append(current_sandwich)

        # again, this is where the program scans if the user inputs a valid sandwich flavour or not
        if sandwichflavours == "Pastrami":
            sandwich_orders.pop()
            print("\nI'm sorry. We don't have any pastrami at the moment.")
            print("Please try again.\n")
            orders = orders - 1
        
        # it's basically the same code as the one above
        elif sandwichflavours != "Pastrami":
            while sandwich_orders:
                current_sandwich = sandwich_orders.pop()
                print("Okay! I made your " + current_sandwich.lower() + " sandwich.")
                finished_sandwich.append(current_sandwich)
    
    elif sandwichflavours != "Pastrami":
        while sandwichesamount != orders:
            orders = orders + 1
            sandwichflavours = input(
                "\nWhat other flavour sandwich would you like? ").title()
            sandwich_orders.append(sandwichflavours)
            
            current_sandwich = sandwich_orders.pop()
            print("Okay! I made your " + current_sandwich.lower() + " sandwich.")
            finished_sandwich.append(current_sandwich)

    print("\nSandwich Orders:\n")
    for sandwich in finished_sandwich:
        print(sandwich + " Sandwich")
    print("\n")