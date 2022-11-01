# Exercise 2:
# Write a Python program to get the Python version you are using.

# right off the bat, i imported "sys" to access code that is available in a different module
# i did this so that i don't have to worry about coding a whole list of things
# (because it is already existing)
import sys

# again, i printed the exercise number for clarification
print("\nExercise 2\n")

# for this exercise, we are told to show the user the python version they are using
# i printed the text below to inform the user what they will see and added "sys.version"
# (which is a code that prints the python system version)
print("The Python version you're using at the moment is " + sys.version)
# i added this extra input line so that the user has a choice to choose whether they want to
# know more or not
# i added "".upper" to make the user's input capitalized no matter what
ans = input("\nWould you like to know about your version information? ").upper

# here, i make use of an if-else statement to print whatever fits the situation
# if the user types "yes", it will be capitalized into "YES"
# now, if the user input matches "YES," the program will print the system version info
# (with the use of the "sys.version_info" command taken from "sys")
if ans == 'YES':
    print("\n", sys.version_info, "\n")
    print("\nThank you. Have a nice day!\n")
# if the user input matches "NO," then the program will print the following and finish the program
elif ans == 'NO':
    print("\nAlright. Have a nice day!\n")
# finally, if the user input doesn't match, then the program will print the following
# and it will ask another time
else:
    ans2 = input("Please only input yes or no: ")
    # here, it's the same thing... it is the same if-else statement above
    if ans == 'YES':
        print("\n", sys.version_info, "\n")
        print("\nThank you. Have a nice day!\n")
    elif ans == 'NO':
        print("\nAlright. Have a nice day!\n")
    else:
        # if the user fails to match the "YES" or "NO" again
        # the program will then print the following
        print("Please reset the program and try again.\n")


