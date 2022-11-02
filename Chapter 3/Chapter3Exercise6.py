# Exercise 6:
# You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests.

# Start with your program from Exercise 3-5.
# Add a new line that prints a message saying that you can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person
# letting them know you’re sorry you can’t invite them to dinner.

# Print a message to each of the two people still on your list, letting them know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.

print("\nExercise 6\n")

# once again, i used the same list also used in exercise 4 and 5
smash = ["bradley simpson", "chris hemsworth", "tom holland", "kit harrington", "jonathan bailey"]

# here, i printed a text letting all guests know that i will be removing some people from the list
print("Dear guests, \nI'm so sorry to say that there isn't enough space for everyone. I would have to reschedule the rest of you for another time. My deepest apologies. Thank you for understanding.\nSincerely, Me\n")

# and after that, i told the program to remove the third, fourth, and fifth guests
# i inputted the popped string in inside a variable and printed a text saying they didn't make the cut
removedguest = smash.pop(2)
print("Dear " + removedguest.title() + "\nI'm sorry to say that you did not ake the cut. I would still love to have you as a guest, let's just work around a schedule that works for us.\n")

removedguest = smash.pop(3)
print("Dear " + removedguest.title() + "\nI'm sorry to say that you did not ake the cut. I would still love to have you as a guest, let's just work around a schedule that works for us.\n")

removedguest = smash.pop(4)
print("Dear " + removedguest.title() + "\nI'm sorry to say that you did not ake the cut. I would still love to have you as a guest, let's just work around a schedule that works for us.\n")

# next, i printed text to the two other guests that are still invited to let them know
print("Dear " + smash[0].title() + "\nI'm happy to inform to that you are still invited for the dinner party on the 16th of November. See you soon!\n")
print("Dear " + smash[1].title() + "\nI'm happy to inform to that you are still invited for the dinner party on the 16th of November. See you soon!\n")

# here, i deleted every string left in the list and printed the list to check if there are still any guests
del smash[0:2]
print(smash)