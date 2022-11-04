# Exercise 5:
# Make a list of your favorite fruits,
# and then write a series of independent if statements that check for certain fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list.
# If the fruit is in your list, the if block should print a statement, such as "You really like bananas!"

print("\nExercise 5\n")

# first off, i made a list of my favourite fruits and named it "favorite_fruits"
favourtie_fruits = ["Sweet Melon", "Strawberry", "Grapes"]

# i created an if-else statement that checks if the string is inside the list...
# if the string is in the list, the program will print the text on line 17, 23, and 26...
# if the string is not in the list, then the program is told to print the text on lines 21 and 30

# note: you might notice that we did not use elif or else...
# that is because we want the program to print them all in one go and if we were to use elif,
# the program would stop at the first true statement
if "Sweet Melon" in favourtie_fruits or "Sweet Melons" in favourtie_fruits:
    print("Wow! You like sweet melons too? They're my favourite fruit!\n")

if "Apple" in favourtie_fruits or "Apples" in favourtie_fruits:
    print("Oh. I like that too, but it's not my favourite.\n")

if "Strawberry" in favourtie_fruits or "Strawberries" in favourtie_fruits:
    print("Wow! You like strawberries too? They're my favourite fruit!\n")

if "Grape" in favourtie_fruits or "Grapes" in favourtie_fruits:
    print("Wow! You like sweet melons too? They're my favourite fruit!\n")

if "Pomegranate" in favourtie_fruits or "Pomegranates" in favourtie_fruits:
    print("Oh. I like that too, but it's not my favourite.\n")