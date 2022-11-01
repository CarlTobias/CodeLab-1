# Exercise 3:
# Tidy up the code to make it easier to understand.

# Use a variable to represent a person’s name,
# and include some whitespace characters at the beginning and end of the name.

# Make sure you use each character combination, “\t” and “\n”, at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions,
# lstrip(), rstrip(), and strip().

print("\nExercise 3\n")

# i assigned a value to a variable,
# (i also used "\t" and "\n" so that i can strip them later on)
c = "\tChris Hemsworth\n"

# here, i printed the variable while using the ".strip()" function
# ".lstrip()" removes the leftmost whitespace character that you can see in the variable
print(c.lstrip())
# ".rstrip()" removes the rightmost whitespace character that you can see in the variable
print(c.rstrip())
# and ".strip()" removes both the left and rightmost whitespace characters
# that you can see in the variable
print(c.strip())