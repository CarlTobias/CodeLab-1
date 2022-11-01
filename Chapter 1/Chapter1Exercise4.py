# Exercise 4:
# Write three strings in different variables and print the output as one string.

# i began by telling the program to print the exercise number
print("\nExercise 4\n")

# i then added variables, which requires user input by using the "input()" function
a = input("Name a random animal: ")
b = input("Name a random food item: ")
c = input("Name a body of water: ")

# i then told the program to print the following:
print("\nWow! All the things you said were my favourite things.\n")
# here, i concatenated text with the user inputs,
# and since the user inputed strings, i did not need to format it like this: "str(x)"
print("My favourite animal is a " + a + ".")
print("My favourite food item is a " + b + ".")
print("My favourite body of water is a " + c + ".")

# i added this thank you note to make the program more user-friendly
print("\nThank you for participating!\n")