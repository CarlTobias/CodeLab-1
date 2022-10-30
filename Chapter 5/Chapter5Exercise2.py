print("\nExercise 2\n")

print("Welcome to the Metaverse Python Programming Glossary!\n")

glossary = {
    "if-else": "The if-else statement is used to execute both the true part and false part of a given condition.",
    "int": "The int() function converts the specified value into an integer number.",
    "print": "The print() function prints the specified message to the screen, or other standard output device."
}

print("The list of Python terms available at the moment are:\n")

for terms in glossary.keys():
    print("- " + terms)

choice = input("\nWhat word do you want defined today? ").upper()

if choice == "PRINT":
    print("print():\n  - " + glossary["print"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

elif choice == "INT":
    print("print():\n  - " + glossary["int"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

elif choice == "IF-ELSE" or choice == "IF ELSE" or choice == "IFELSE":
    print("print():\n  - " + glossary["if-else"])
    print("\nThank you for using our glossary! See you soon.")
    feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
    print("\nThank you!")

else:
    print("Oh, I'm sorry. Our glossary is still being updated. Try that word again soon.\n")

    choice2 = input("Would you like to define another word? ").upper()

    if choice2 == "YES":
        choice = input("\nWhat word do you want defined? ").upper()
        
        if choice == "PRINT":
            print("print():\n  - " + glossary["print"])
            print("\nThank you for using our glossary! See you soon.")
            feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
            print("\nThank you!")
        
        elif choice == "INT":
            print("print():\n  - " + glossary["int"])
            print("\nThank you for using our glossary! See you soon.")
            feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
            print("\nThank you!")
        
        elif choice == "IF-ELSE" or choice == "IF ELSE" or choice == "IFELSE":
            print("print():\n  - " + glossary["if-else"])
            print("\nThank you for using our glossary! See you soon.")
            feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
            print("\nThank you!")
        
        else:
            print("\nI'm sorry, we still haven't added that word yet as well. Please try again soon!")
    
    elif choice2 == "NO":
        print("\nAlright. Thank you! See you soon.")

    else:
        choice2 = input("\nYes or No? ").upper()

        if choice2 == "YES":
            choice = input("\nWhat word do you want defined? ").upper()
            
            if choice == "PRINT":
                print("print():\n  - " + glossary["print"])
                print("\n\nThank you for using our glossary! See you soon.")
                feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            elif choice == "INT":
                print("print():\n  - " + glossary["int"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            elif choice == "IF-ELSE" or choice == "IF ELSE" or choice == "IFELSE":
                print("print():\n  - " + glossary["if-else"])
                print("\nThank you for using our glossary! See you soon.")
                feedback = input("\n\nPlease tell us what more we could do to enhance your experience.\nFeedback: ")
                print("\nThank you!")

            else:
                print("\nI'm sorry, we still haven't added that word yet as well. Please try again soon!")
        
        elif choice2 == "NO":
            print("\nAlright. Thank you! See you soon.")
        
        else:
            print("\nUh oh, It looks like you made a booboo. Please reset the program and try again.\n")