# Exercise 2:
# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.

# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning,
# or print the word on one line and then print its meaning indented on a second line.
# Use the newline character(\n) to insert a blank line between each word-meaning pair in your output.
print("\nExercise 2\n")

# i created a user-defined function called "repeat()"
# i did this to lessen the code below, because the code would be too lengthy
def repeat():
    # inside this function, it starts with a "while" function...
    # while "choice" is not true, then it will keep repeating the block of code under it
    while choice != True:
        # first, it would ask the user if they want to define another word
        choice2 = input("Would you like to define another word? ").upper()

        # if yes, then it will continue to ask what word the user wants to define
        if choice2 == "YES":
            choice = input("\nWhat word do you want defined? ").upper()

            # the program will then check this if-else statement (used later on)...
            # i didn't input this in a user-defined function
            # because there are some details here that are not used in the first if-else statement
            if choice == "DEF" or choice == "USER-DEFINED FUNCTION" or choice == "USER DEFINED FUNCTION" or choice == "USER-DEFINED FUNCTIONS" or choice == "USER DEFINED FUNCTIONS":
                print("def():\n  - " + glossary["def"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input(
                    "\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            elif choice == "IF-ELSE" or choice == "IF ELSE" or choice == "IFELSE":
                print("if-else:\n  - " + glossary["if-else"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input(
                    "\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            elif choice == "INT":
                print("int:\n  - " + glossary["int"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input(
                    "\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            elif choice == "PRINT":
                print("print():\n  - " + glossary["print"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input(
                    "\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            elif choice == "WHILE":
                print("while:\n  - " + glossary["while"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input(
                    "\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            else:
                print(
                    "\nI'm sorry, we still haven't added that word yet as well. Please try again\n!")

        # now if the user inputs "NO," the program will print the text below
        # and finish the program (using the break statement)
        elif choice2 == "NO":
            print("\nAlright. Thank you! See you soon.\n")
            break;
        
        # if the user inputs anything other than "YES" or "NO,"
        # then the program will print the following text and call the function again
        else:
            choice2 = input("\nYes or No? ").upper()
            # i called the function here again to basically make it infinite...
            # the user can mess up as many times they want, and i don't have to keep repeating
            # the same if-else statements over and over again
            repeat()

# once again, the user is welcomed (because we have to be welcoming ;>) before anything else
print("Welcome to the Metaverse Python Programming Glossary!\n")

# next, i defined a dictionary, and inputted Python terms that I've learned throughout the semester
glossary = {
    # (it's put neatly in alphabetical order because i'm neat like that hehe)
    "def()": "The def() function is used to help shorten long codes. The programmer can make user-defined functions to avoid repeating lenghty and repetitive codes.",
    "if-else": "The if-else statement is used to execute a certain line of command depending on the underlying condition.",
    "int": "The int() function converts a specific value into an integer number.",
    "print": "The print() function prints specific texts to the user's output screen.",
    "while": "The while loop is used to repeat a block of code so long as the condition is true."
}

# here is text that shows the list of available terms that can be defined by the program
print("The list of Python terms available at the moment are:\n")

# i used a "for" loop to get the list of available terms
for terms in glossary.keys():
    print("- " + terms)

# now here, the program is asking for a term the user wants defined
# you can see that i assigned a variable (named "choice") to the input function
# and i also added ".upper()" to ensure the input is the same as the conditions later on
choice = input("\nWhat word do you want defined today? ").upper()

# now here is where the if-else statement starts...
# each if and elif block has its own word/term to define

# if user's input equals the condition below,
if choice == "DEF" or choice == "USER-DEFINED FUNCTION" or choice == "USER DEFINED FUNCTION" or choice == "USER-DEFINED FUNCTIONS" or choice == "USER DEFINED FUNCTIONS":
    # the program will run this block of code
    print("def():\n  - " + glossary["def"])
    print("\nThank you for using our glossary! See you soon.")
    # in the line below, i added a feedback feature to make the user more engaged with the program
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

# it's the same for all of these elif statements
elif choice == "IF-ELSE" or choice == "IF ELSE" or choice == "IFELSE":
    print("if-else:\n  - " + glossary["if-else"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

elif choice == "INT":
    print("int:\n  - " + glossary["int"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

elif choice == "PRINT":
    print("print():\n  - " + glossary["print"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

elif choice == "WHILE":
    print("while:\n  - " + glossary["while"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

# now, in case the user gives an invalid input, the program will follow this else statement
else:
    # the program is told to print text apologizing to the user
    # because the word/term has not been added yet
    print("Oh, I'm sorry. Our glossary is still being updated. Try that word again soon.\n")
    
    # i called the user-defined function here (which saves a lot time and space)
    repeat()