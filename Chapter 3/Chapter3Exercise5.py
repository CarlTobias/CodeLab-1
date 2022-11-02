# Exercise 5:
# You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can’t make it.

# Modify your list,
# replacing the name of the guest who can’t make it with the name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is still in your list.

print("\nExercise 5\n")

# i used the same list as the previous exercise
smash = ["bradley simpson", "chris hemsworth", "tom holland", "kit harrington", "jonathan bailey"]

# and finally, i printed the same text as the previous exercise again letting them know they're still invited
print("Dear " + smash[0].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[1].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[2].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[3].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[4].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")

# i printed text saying that i'm sorry to hear about the decline to my invitation
print("Dear " + smash[3] + ",\nI'm sorry to hear that you cannot come to the party. I hope to see you soon.")

# and so here, i replaced the 4th string from "kit harrington" to "kit connor"
smash[3] = "kit connor"

# and i printed this text once again to show that the one guest has been replaced
print("Dear " + smash[0].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[1].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[2].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[3].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
print("Dear " + smash[4].title() + ",\nI will be holding a dinner party on the 16th of November. I would like to inform you that you are invited to come. Please send a message to confirm your attendance. Hope to see you there!\nSincerely, Me\n")
