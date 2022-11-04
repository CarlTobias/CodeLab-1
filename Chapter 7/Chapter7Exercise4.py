# Exercise 4:
# Modify the make_shirt() function so that shirts are large by default
# with a message that reads "I love Python."
# Make a large shirt and a medium shirt with the default message, and a shirt
# of any size with a different message.

print("\nExercise 4:\n")

# i copied the function i made in the previous exercise
def makeshirt(size = "large", message = "I love Python!"):
    print("\nThe size of your shirt will be " + str(size) + " and the message on the shirt will be '" + str(message) + ".'\n")

# here, i called the function as is, so it's the default (like the previous exercise)
makeshirt()
# the second time i called the function, i changed the size to medium instead of the default "large."
makeshirt(size = "medium")
# and here, i called the function with input so that the user can put any size and message
makeshirt(input("What would your shirt size be? "), input("What message would you want for your shirt? "))