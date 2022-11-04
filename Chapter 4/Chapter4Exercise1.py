# Exercise 1:

# Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# Write an if statement to test whether the alien’s color is green.
# If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails.
# (The version that fails will have no output.)

print("\nExercise 1\n")

# first, i added some text that adds some story (for fun ehehe)
print("There are rabid dogs surrounding us.")
print("Three of them are aliens in disguise, but the green one is their leader and we must kill it to kill the rest.\n")
print("Quick!! Pick an alien to shoot.")

# i added a variable named "alien_color" to store input from user
# for the input, i ask the user to pick a number from 1 to 3
alien_color = int(input("Which alien are you gonna shoot? 1, 2, or 3? "))

# i started an if-else statement to accommodate for every situation that could happen
if (alien_color == 1):
    # if the user inputs "1," then the user will get this message:
    print("\n\nOh no! You shot the yellow alien (the scientist) and the other two ate you.\n")
    print("Game Over.\n")

elif (alien_color == 2):
    # if the user inputs "2," then the user will get this message:
    print("\n\nYaaass!! You did it. You killed the green alien (the mastermind) and the other two died as well.\n")
    print("You move forward and you encounter 5 werewolves.\n")
    print("To be continued...\n")

elif (alien_color == 3):
    # if the user inputs "3," then the user will get this message:
    print("\n\nOh no! You shot the red alien (the lieutenant) and the other two ate you.\n")
    print("Game Over.\n")

else:
    # and finally, if the user inputs anything else other than the given choices, the program will print:
    print("\n\nOh no! You broke the game.\n")
    print("Reset Program.\n")
