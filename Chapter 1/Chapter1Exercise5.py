# Exercise 5:
# Write a Python program which accepts the radius of a circle from the user and compute the area.

# i started things off by importing the "math" module and specifically taking "pi"
from math import pi

# as usual, i told the program to print the exercise number before anything else
print("\nExercise 5\n")

# i also told the program to print a welcome greeting to let the user know what the program is
print("Hello! Welcome to the C.I.R.C.L.E Computer!\n")

# here, i named a variable "radius," and asked the user to input the radius into said variable
radius = float (input("What is the radius of your cirle? "))

# then, i told the program to follow this formula, using the given input and the imported pi...
# it was then stored in a variable named "area"
area = float(pi*(radius**2))

# then, i asked the program to print the following:
print("The area of your circle with the radius", radius, "is", area)
# compared to the previous exercise, the concatenation of the text here is different...
# instead of using "+", we used commas(,)...
# it's technically the same as using plus (with minor differences only)

# and finally, i told the program to print this goodbye message foa a more user-friendly experience
print("\nHave a great day!\n")
