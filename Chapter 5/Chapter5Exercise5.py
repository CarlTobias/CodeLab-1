# Exercise 5:
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.

print("\nExercise 5\n")

# first i created a list for a pet dog called "canines"
canines = {
    "Owner's Name" : "Amihan Anderson",
    "Breed" : "Siberian Husky",
    "Pet Name" : "Bark Obama",
    "Pet Age" : "4"
}

# and another for a pet cat called "felines"
felines = {
    "Owner's Name": "Samantha Renee",
    "Breed": "Ragdoll",
    "Pet Name": "Doja",
    "Pet Age": "2"
}

# and one more for a pet snake called "reptiles"
reptiles = {
    # each dictionary has a key-value pair for the owner's name, pet/animal breed, pet name and age
    "Owner's Name": "Kyle Reeferson",
    "Breed": "Ball Python",
    "Pet Name": "Ekans",
    "Pet Age": "6"
}

# now, i made a list containing the dictionaries
pets = [canines, felines, reptiles]

# and in this "for" loop, the program scans for each item in the list "pets"
for animals in pets:
    # it prints the following text:
    print("\nDetails:\n")
    # and starts another "for" loop scanning for every key-value pairs in the dictionaries
    for infoneeded, infogiven in animals.items():
        # and prints them neatly (according to how i formatted it)
        print(infoneeded + ": " + infogiven)