# Exercise 3:
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99)
# by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.

# When you’re sure that your loop works, add five more Python terms to your glossary.

# When you run your program again,
# these new words and meanings should automatically be included in the output.

print("\nExercise 3\n")

# alright, here its the same dictionary as the previous, only this time, i added more words/terms
glossary = {
    "and" : "This is one of many boolean operators in Python. It allows you to create compound boolean expressions that you can use to decide actions to be done in a program.",
    "def()": "The def() function is used to help shorten long codes. The programmer can make user-defined functions to avoid repeating lenghty and repetitive codes.",
    "dictionary" : "It is used to store data in key:value pairs.",
    "for" : "The for loop is used to loop through iterable objects (like lists) and then perform the same task for every value in that object.",
    "if-else": "The if-else statement is used to execute a certain line of command depending on the underlying condition.",
    "int": "The int() function converts a specific value into an integer number.",
    "or": "This is one many boolean operators in Python. It returns the first or last object that is true or in an expression (regardless of the truth value).",
    "print": "The print() function prints specific texts to the user's output screen.",
    "variables" : "A variable is something in which an object can be assigned to. In layman's terms, it holds data that is to be used inside a program.",
    "while": "The while loop is used to repeat a block of code so long as the condition is true."
}

# and of course, we have to welcome the user
print("Welcome to the Metaverse Python Programming Glossary!\n")

# unlike the previous task, i a not going to ask for user input here...
# i used a for loop to print the keys and values of the dictionary in a neater way,
# and so that it prints all together instead of letting the user type a specific word
for terms, meanings in glossary.items():
    print(terms + "\n- " + meanings + "\n")