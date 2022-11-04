# Exercise 2:
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as "One of my favorite books is Alice in Wonderland."
# Call the function, making sure to include a book title as an argument in the function call.

print("\nExercise 2\n")

# here, i defined a function called "favbook" and defining a variable in it called "comicbook"
def favbook(comicbook):
    # when the function is called, the program will print a text while also using the variable "comicbook"
    print("My favourite book at the moment is " + comicbook + ".\n")

# here, i called the function "favbook()" but instead of just the 
favbook(input("What is your favourite book? "))