from traceback import print_tb


print("\nExercise 5\n")

print("Narration: A girl heads to a computer shop to buy some USB sticks. \nShe loves USB sticks and wants as many as she can get for £50. They are £6 each.\n")

print("Girl: How much for a USB stick?")
print("Store Owner: Just £6!")
usbstick = 6

print("Girl: Oh cool! I'd like to buy all the USB sticks that can fit in my budget please.")
budget = 50
amountofusbsticks = budget//usbstick

pricetopay = usbstick*amountofusbsticks
change = 50%6

print("Store Owner: Okay! That will be £" + str(pricetopay) + " for " + str(amountofusbsticks) + " USB sticks please.")
print("Girl: Here you go sir! Here's £" + str(budget) + ".")
print("Store Owner: Alright! Your change is £" + str(change) + ". Thank you very much for shopping with us today.")
print("Girl: Thank you! See you soon :)\n")
