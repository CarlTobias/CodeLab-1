print("\nExercise 5\n")

canines = {
    "Owner's Name" : "Amihan Anderson",
    "Breed" : "Siberian Husky",
    "Pet Name" : "Bark Obama",
    "Pet Age" : "4"
}

felines = {
    "Owner's Name": "Samantha Renee",
    "Breed": "Ragdoll",
    "Pet Name": "Doja",
    "Pet Age": "2"
}

reptiles = {
    "Owner's Name": "Kyle Reeferson",
    "Breed": "Ball Python",
    "Pet Name": "Ekans",
    "Pet Age": "6"
}

pets = [canines, felines, reptiles]

for animals in pets:
    print("\nDetails:\n")
    for infoneeded, infogiven in animals.items():
        print(infoneeded + ": " + infogiven)