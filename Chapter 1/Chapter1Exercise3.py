# Exercise 3:
# Write a Python program to display the current date and time.

# from here, i imported another program again, but this time i only took a specific part
# i took the "date" part because i want to first focus on printing dates
from datetime import date
# after importing, i used the commands to check for the date today and also added a varaible
# to hold it, the "%B %d, %Y" part indicates the layout for printing the date
daytoday = date.today().strftime("%B %d, %Y")

# i then imported another part of "datetime," but this time im focusing on the time
from datetime import datetime
# i did the same thing as the first part, i added a variable, then used commands from the module
timerightnow = datetime.now().time().strftime('%H:%M')

# like the last two exercises, i printed the exercise number
print("\nExercise 3\n")

# i then told the program to print the following:
print("The date today is", daytoday)
print("The time at the moment is", timerightnow)
print("\nHave a nice day!\n")