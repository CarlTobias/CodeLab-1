import sys

print("\nExercise 2\n")

print("The Python version you're using at the moment is " + sys.version)
ans = input("\nWould you like to know about your version information? (Answer only Y or N.) ")

if ans == 'Y':

    print("\n", sys.version_info, "\n")
    print("\nThank you. Have a nice day!\n")
elif ans == 'N':
    
    print("\nAlright. Have a nice day!\n")

