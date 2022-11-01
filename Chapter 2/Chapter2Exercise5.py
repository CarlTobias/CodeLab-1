# Exercise 5:
# A girl heads to a computer shop to buy some USB sticks.
# She loves USB sticks and wants as many as she can get for £50. They are £6 each.

# Write a programme that calculates how many USB sticks she can buy
# and how many pounds she will have left.
# You are to use the arithmetic operators to complete this exercise.

print("\nExercise 5\n")

# to start, i made it into a story to make it more engaging

# i told the program to print the following lines:
print("Narration: A girl heads to a computer shop to buy some USB sticks. \nShe loves USB sticks and wants as many as she can get for £50. They are £6 each.\n")

print("Girl: How much for a USB stick?")
print("Store Owner: Just £6!")
# i then assigned values to variables in order that they appear in the story
usbstick = 6

print("Girl: Oh cool! I'd like to buy all the USB sticks that can fit in my budget please.")
budget = 50
# below, you can see the formulas that the program will follow
amountofusbsticks = budget//usbstick

pricetopay = usbstick*amountofusbsticks
change = 50%6

# in here, i continued the story and also concatenated the results from the formula above
print("Store Owner: Okay! That will be £" + str(pricetopay) + " for " + str(amountofusbsticks) + " USB sticks please.")
print("Girl: Here you go sir! Here's £" + str(budget) + ".")
print("Store Owner: Alright! Your change is £" + str(change) + ". Thank you very much for shopping with us today.")
print("Girl: Thank you! See you soon :)\n")
