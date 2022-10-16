print("\nExercise 1\n")

print("There are rabid dogs surrounding us.")
print("Three of them are aliens in disguise, but the green one is their leader and we must kill it to kill the rest.\n")
print("Quick!! Pick an alien to shoot.")

alien_color = int(input("Which alien are you gonna shoot? 1, 2, or 3? "))

if (alien_color == 1):
    print("\n\nOh no! You shot the yellow alien (the scientist) and the other two ate you.\n")
    print("Game Over.\n")

elif (alien_color == 2):
    print("\n\nYaaass!! You did it. You killed the green alien (the mastermind) and the other two died as well.\n")
    print("You move forward and you encounter 5 werewolves.\n")
    print("To be continued...\n")

else:
    print("\n\nOh no! You shot the red alien (the lieutenant) and the other two ate you.\n")
    print("Game Over.\n")
