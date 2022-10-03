from datetime import date
daytoday = date.today().strftime("%B %d, %Y")

from datetime import datetime
timerightnow = datetime.now().time().strftime('%H:%M')

print("\nExercise 3\n")

print("The date today is", daytoday)
print("The time at the moment is", timerightnow)
print("\nHave a nice day!\n")
