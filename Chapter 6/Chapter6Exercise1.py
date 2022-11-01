# Exercise 1:
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

print("\nExercise 1\n")

# to start, i assigned a variable to store user input
# and printed the text below to inform the user that the topping has been added
pizzatoppings = input("Please enter a pizza topping you'd like to add: ").title()
print("Great! " + pizzatoppings + " has been added to your pizza.\n")

# i then started a "while" loop

# this loop will continue until the user inputs "No"

# basically the line of code below says,
# "As long as the variable "pizzatoppings" doesn't have the value "No," then it will coninue forever"
# note: "!=" means "does not equal to"
while pizzatoppings != "No":
    # inside the loop, we see basically the same thing as the first two codes above,
    # but with a bit of changes
    pizzatoppings = input("Alright, are there any more? (Enter 'no' to finish order): ").title()
    print("Great! " + pizzatoppings + " has been added to your pizza.\n")

# when the user finally finishes, the program will print this:
print("Thank you! Please wait for your order for about 10 minutes.\n")
