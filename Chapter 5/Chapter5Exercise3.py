print("\nExercise 3\n")

glossary = {
    "and" : "This is one of the three boolean operators in Python. It allows you to construct compound boolean expressions that you can use to decide the course of actions to be done in your program.",
    "def()": "The def() function is used to help shorten long codes. Instead of repeating codes, a programmer can make a user-defined function to shorten the overall length of a program.",
    "dictionary" : "It is used to store data in key:value pairs.",
    "for" : "The for loop is used to loop through iterable objects (like lists) and perform the same task for every entry in that object.",
    "if-else" : "The if-else statement is used to execute both the true part and false part of a given condition.",
    "int" : "The int() function converts the specified value into an integer number.",
    "or": "This is one of the three boolean operators in Python. It returns the first object that evaluates to true or the last object in the expression (regardless of the truth value).",
    "print" : "The print() function prints the specified message to the screen, or other standard output device.",
    "variables" : "A variable is something in which an object can be assigned to. In layman's terms, it holds data that is to be used inside a program.",
    "while" : "The while loop is used to iterate a block of code so long as the condition is true."
}

print("Welcome to the Metaverse Python Programming Glossary!\n")

for terms, meanings in glossary.items():
    print(terms + "\n- " + meanings + "\n")