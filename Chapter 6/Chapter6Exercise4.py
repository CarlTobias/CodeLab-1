# Exercise 4:
# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.

# Loop through the list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich. As each sandwich is made,
# move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.


print("\nExercise 4\n")

# i first welcome the user with the text below, then proceeded with the program
print("Welcome to The New Deli!\n")

# similar to what i did in exercise 2, i assigned two variables for a "while" loop
# (to determine how many times i want the program to ask the user their wanted sandwich flavor/s)
sandwichesamount = int(input("How many sandwiches would you like to order? "))
orders = 1

# i also created two lists here...
# (one for pending sandwich orders and one for finished sandwiches)
sandwich_orders = []
finished_sandwich = []

# i started an if-else statement

# if the user only wants one sandwich to order, the block of code under the if statement...
if sandwichesamount == 1:

    # (the workings behind this whole block is explained below... continue to line 45)
    sandwichflavours = input("\nWhat flavour sandwich would you like? ").title()
    sandwich_orders.append(sandwichflavours)

    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print("Okay! I made your " + current_sandwich.lower() + " sandwich.\n")
        finished_sandwich.append(current_sandwich)

        print("Sandwich Orders:\n")

        for sandwich in finished_sandwich:
            print(sandwich + " Sandwich")

# otherwise, it will run this block of code
else:
    # now inside this block, i told the program to ask the user for the user's first order...
    # (you can also find this exact same code on lines 32 and 33)
    sandwichflavours = input("\nWhat flavour sandwich would you like? ").title()
    # after which the program will add the inputted value inside one of the empty lists created earlier
    # (the empty list of pending sandwiches)
    sandwich_orders.append(sandwichflavours)

    # this line removes the first pending sandwich and removes it from the current list,
    # add to a variable named current_sandwich
    current_sandwich = sandwich_orders.pop()
    # and from here, it prints the first sandwich with the following text:
    print("Okay! I made your " + current_sandwich.lower() + " sandwich.\n")
    # and puts the data from "current_sandwich" to "finished_sandwich"
    # (this is the second empty list)
    finished_sandwich.append(current_sandwich)

    # here, i started the "while" loop that asks the user for another sandwich
    # (for a specified amount of times)
    while sandwichesamount != orders:
        orders = orders + 1
        # this line of code also asks for a sandwich flavour
        # (but in a different way to make it less repetitive)
        sandwichflavours = input("\nWhat other flavour sandwich would you like? ").title()
        # it also adds the data to the empty list of pending sandwiches
        sandwich_orders.append(sandwichflavours)

        # now this loop will repeat as long as the list "sandwich_orders" is not empty
        while sandwich_orders:
            # this block is just a repetition of lines 56, 58, and 61
            current_sandwich = sandwich_orders.pop()
            print("Okay! I made your " + current_sandwich.lower() + " sandwich.\n")
            finished_sandwich.append(current_sandwich)

    # i then printed this line to indicate that im about to list all finished sandwich orders
    print("Sandwich Orders:\n")

    # now this loop says that for every sandwich in the list "finished_sandwich,"
    # it will execute the block of code within the loop
    for sandwich in finished_sandwich:
        print(sandwich + " Sandwich")
        
    # and finally i told the program to print a newspace to make it look better when running
print("\n")