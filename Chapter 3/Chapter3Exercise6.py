print("\nExercise 6\n")

smash = ["bradley simpson", "chris hemsworth", "tom holland", "kit harrington", "jonathan bailey"]

print("Dear guests, \nI'm so sorry to say that there isn't enough space for everyone. I would have to reschedule the rest of you for another time. My deepest apologies. Thank you for understanding.\nSincerely, Me\n")

removedguest1 = smash.pop(4)
removedguest2 = smash.pop(3)
removedguest3 = smash.pop(2)


print("Dear " + removedguest1.title() + "\nI'm sorry to say that you did not ake the cut. I would still love to have you as a guest, let's just work around a schedule that works for us.\n")
print("Dear " + removedguest2.title() + "\nI'm sorry to say that you did not ake the cut. I would still love to have you as a guest, let's just work around a schedule that works for us.\n")
print("Dear " + removedguest3.title() + "\nI'm sorry to say that you did not ake the cut. I would still love to have you as a guest, let's just work around a schedule that works for us.\n")
print("Dear " + smash[0].title() + "\nI'm happy to inform to that you are still invited for the dinner party on the 16th of November. See you soon!\n")
print("Dear " + smash[1].title() + "\nI'm happy to inform to that you are still invited for the dinner party on the 16th of November. See you soon!\n")

del smash[0:2]
print(smash)