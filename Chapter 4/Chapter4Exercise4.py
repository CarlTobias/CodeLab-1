print("\nExercise 4\n")

print("Wlcome to the Life Stage Determiner!\n")

age = input("Enter age: ")

if age < 2:
    print("You are a baby. GooGooGahGah.")

elif age >= 2:
    print("You are a toddler. Wah Wah.")

elif age <= 4:
    print("You are a kid. Enjoy every moment. Adulthood sucks.")

elif age <= 13:
    print("You are a teen. Stop making everyone so miserable.")

elif age <= 20:
    print("Ew. You are an adult. Go get a job.")

elif age >= 65:
    print("You are an elder. Gimme some wisdom Gramps/Grams!")

else:
    age = ("Please enter a number: ")

    if age < 2:
        print("You are a baby. GooGooGahGah.")
    
    elif age >= 2:
        print("You are a toddler. Wah Wah.")
    
    elif age <= 4:
        print("You are a kid. Enjoy every moment. Adulthood sucks.")
    
    elif age <= 13:
        print("You are a teen. Stop making everyone so miserable.")
    
    elif age <= 20:
        print("Ew. You are an adult. Go get a job.")
    
    elif age >= 65:
        print("You are an elder. Gimme some wisdom Gramps/Grams!")
    
    else:
        print("Aww, you broke it. Please reset the program.")