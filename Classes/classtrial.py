# note: this file is rough notes...
# it may not be complete, or look messy, but this is just a preview of how i learn practically

print("Try not to cry,")
print("I won't say goodbye")
print("Just yet...")
print("So hold on to my hands")
print("Oh I'll be fine")
print("For tonight")
print("With you by my side")
print("Don't you know you're my lifeline.")


import sys
print("Python Version: ")
print(sys.version)

print("Version Info: ")
print(sys.version_info)


from datetime import date

today = date.today()
print("Today's date is", today)

d2 = today.strftime("%B %d, %Y")
print("The date today is", d2)

from datetime import datetime

now = datetime.now()

print("It is now", now, "in your area.")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Date and Time:", dt_string)

print("hi.")