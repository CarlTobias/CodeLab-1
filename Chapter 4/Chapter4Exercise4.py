# Exercise 4:
# Write an if-elif-else chain that determines a person’s stage of life.
# Set a value for the variable age, and then:

# If the person is less than 2 years old, print a message that the person is a baby.

# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

# If the person is at least 4 years old but less than 13, print a message that the person is a kid.

# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

# If the person is at least 20 years old but less than 65, print a message that the person is an adult.

# If the person is age 65 or older, print a message that the person is an elder.

print("\nExercise 4\n")

# first off, as usual, i told the program to print text that greets the user
print("Welcome to the Life Stage Determiner!\n")

# i then made a variable to store an integer value for user input
age = int(input("Enter age: "))

# now, here's the beginning of a very lengthy if-else statement
# it starts by checking if the user-input variable is less than 2
if age < 2:
    # if that statement is true, then the program will print:
    print("You are a baby. GooGooGahGah.")

# if the statement above is false,
# then the program will check if "age" (the user input value) is less than 4
elif age < 4:
    # if that statement is true, then the program will print:
    print("You are a toddler. Wah Wah.")

# if the statement above is false,
# then the program will check if "age" (the user input value) is less than 13
elif age < 13:
    # if that statement is true, then the program will print:
    print("You are a kid. Enjoy every moment. Adulthood sucks.")

# if the statement above is false,
# then the program will check if "age" (the user input value) is less than 20
elif age < 20:
    # if that statement is true, then the program will print:
    print("You are a teen. Stop making everyone so miserable.")

# if the statement above is false,
# then the program will check if "age" (the user input value) is less than 65
elif age < 65:
    # if that statement is true, then the program will print:
    print("Ew. You are an adult. Go get a job.")

# if the statement above is false,
# then the program will check if "age" (the user input value) is greater than 65
elif age > 65:
    # if that statement is true, then the program will print:
    print("You are an elder. Gimme some wisdom Gramps/Grams!")


# now here, if the user inputs any invalid age (anything under -1 or over 120)...
elif age <= -1 or age > 120:
    # then the program will execute the following commands
    age = int(input("Please enter a valid age: "))

    # here is another iteration of the if-else statement at the start
    if age < 2:
        print("You are a baby. GooGooGahGah.")
    
    elif age < 4:
        print("You are a toddler. Wah Wah.")
    
    elif age < 13:
        print("You are a kid. Enjoy every moment. Adulthood sucks.")
    
    elif age < 20:
        print("You are a teen. Stop making everyone so miserable.")
    
    elif age < 65:
        print("Ew. You are an adult. Go get a job.")
    
    elif age > 65:
        print("You are an elder. Gimme some wisdom Gramps/Grams!")
    
    # the second time that the user inputs an inavlid age,
    # then the user would have to reset the program
    elif age <= -1 or age > 120:
        # this is the line that will be printed
        print("Aww, you broke it. Please reset the program.")