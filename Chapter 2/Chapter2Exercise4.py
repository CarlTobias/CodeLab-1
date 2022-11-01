# Exercise 4:
# Use a variable to represent your favorite number.
# Then, using that variable, create a message that reveals your favorite number.
# Print that message.

print("\nExercise 4\n")

# here, i asked the user to enter their favourite number
# to ensure that the user can only input numbers, i added "float()" outside "input()"
favnum = float(input("Enter your ABSOLUTE favorite number: "))

# then, i told the program to print the following line:
print("No way!! My ABSOLUTE favourite number is " + str(favnum) + "too!\n")
# you can see that the concatenated variable has "str()"
# that is because it is not possible to concatenate strings with integers or floats
