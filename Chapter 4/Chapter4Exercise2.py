# Exercise 2:
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

# If the alien’s color is green,
# print a statement that the player just earned 5 points for shooting the alien.

# If the alien’s color isn’t green, print a statement that the player just earned 10 points.

# Write one version of this program that runs the if block and another that runs the else block.

print("\nExercise 2\n")

# first off, i printed a statement welcoming the user to the "alien shooting range"
print("Welcome to the alien shooting range!")

# next, i made a variable to store value for user input
alien_color = str(input("Shoot a green or red alien: "))

# and here, i started an if-else statement to accommodate possible outcomes in the program
# you can also see here, i added ".upper()" to ensure the user input is all caps
if (alien_color.upper() == "GREEN"):
    # if the user picks "GREEN," they will get 5 points
    print("\n\n+5 Points\n")
    # and here, the program asks the user to shoot another alien
    alien_color2 = str(input("Shoot another one: "))
    # here, is similar to the main if-else block...
    # the only difference is that it uses a different variable
    if (alien_color2.upper()) == "GREEN":
        print("\n\n+5 Points\n")

    elif (alien_color2.upper() == "RED"):
        print("\n\n+20 Points\n")

    else:
        print("\n\nOh no! It looks like you hacked the game. Game Over.\n")


elif (alien_color.upper() == "RED"):
    # if the user picks "RED," they will receive 20 points...
    print("\n\n+20 Points\n")
    # and will be asked to shoot another alien
    alien_color2 = str(input("Shoot another one: "))
    # again, this is also similar to the original if-else block, it just uses a different variable
    if (alien_color2.upper()) == "GREEN":
        print("\n\n+5 Points\n")

    elif (alien_color2.upper() == "RED"):
        print("\n\n+20 Points\n")

    else:
        print("\n\nOh no! It looks like you hacked the game. Game Over.\n")


# now, if the user picks any other color other than "RED" or "GREEN,"
# the program will execute the commands under the else block
else:
    print("\n\nOh no! It looks like you hacked the game. Game Over.\n")
