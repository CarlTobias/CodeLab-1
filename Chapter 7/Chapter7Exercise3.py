# Exercise 3:
# Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt. The function should print a sentence
# summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

print("\nExercise 3:\n")

# first, i defined a function "makeshirt" that has two parameters "size" and "message"

def makeshirt(size = "large", message = "I love Python!"):
    # like the previous exercises in this chapter, i inputted commands inside the function,
    # so that i can call it at any time without having to tediously repeating commands
    print("\nThe size of your shirt will be " + str(size) + " and the message on the shirt will be '" + str(message) + ".'\n")

# outside the function, i called the function like in exercise 2, but here,
# i didn't include the input function because i wanted it to print the default message
makeshirt()

# if you want some extra points you could do it like this:
makeshirt(input("What would your shirt size be? "), input("What message would you want for your shirt? "))
# i called the function again, but this time, i'm adding two inputs for the two parameters
# (so we can change the default)