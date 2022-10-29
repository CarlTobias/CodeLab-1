print("\nExercise 3\n")

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

elif (alien_color.upper() == "YELLOW"):
    print("\n\n+10 Points\n")
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
