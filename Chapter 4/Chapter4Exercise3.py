# Exercise 3:
# Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

# If the alien is green, print a message that the player earned 5 points.

# If the alien is yellow, print a message that the player earned 10 points.

# If the alien is red, print a message that the player earned 15 points.

# Write three versions of this program,
# making sure each message is printed for the appropriate color alien.

print("\nExercise 3\n")

# alright, so in this task, the codes are the same with the previous exercise,
# so i will not be going over the codes i explained before
print("Welcome to the alien shooting range!")

alien_color = str(input("Shoot a green, red, or yellow alien: "))

if (alien_color.upper() == "GREEN"):
    print("\n\n+5 Points\n")
    alien_color2 = str(input("Shoot another one: "))

    if (alien_color2.upper()) == "GREEN":
        print("\n\n+5 Points\n")

    elif (alien_color2.upper() == "RED"):
        print("\n\n+20 Points\n")

    elif (alien_color2.upper() == "YELLOW"):
        print("\n\n+10 Points\n")

    else:
        print("\n\nOh no! It looks like you hacked the game. Game Over.\n")


elif (alien_color.upper() == "RED"):
    print("\n\n+20 Points\n")
    alien_color2 = str(input("Shoot another one: "))

    if (alien_color2.upper()) == "GREEN":
        print("\n\n+5 Points\n")

    elif (alien_color2.upper() == "RED"):
        print("\n\n+20 Points\n")

    elif (alien_color2.upper() == "YELLOW"):
        print("\n\n+10 Points\n")

    else:
        print("\n\nOh no! It looks like you hacked the game. Game Over.\n")

# so for this part, it's essentially the same if-else block as before,
# only this time, it's for the color "YELLOW"
elif (alien_color.upper() == "YELLOW"):
    # the user will receive 10 points
    print("\n\n+10 Points\n")
    # the user will also get to shoot another alien (just like the other if-else blocks)
    alien_color2 = str(input("Shoot another one: "))

    if (alien_color2.upper()) == "GREEN":
        print("\n\n+5 Points\n")

    elif (alien_color2.upper() == "RED"):
        print("\n\n+20 Points\n")

    elif (alien_color2.upper() == "YELLOW"):
        print("\n\n+10 Points\n")

    else:
        print("\n\nOh no! It looks like you hacked the game. Game Over.\n")

else:
    print("\n\nOh no! It looks like you hacked the game. Game Over.\n")
