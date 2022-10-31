# first, i defined a class style for color
class style:
    # as you can see here, i used the ANSI codes
    BOLD = '\033[1m'
    END = '\033[0m'

# here, i printed the exercise number
# (you'll be seeing this in every activity that i will have passed)
print("\nExercise 1\n")

# for this print command, i added a "style.BOLD" before the actual text
# i did this to make the text bold
# you can also see "4m\033," this is part of the ANSI codes for the colors
# the "\n" is a command used for a new line
# and finally, i used "style.END" to tell the program that i only want text bold until that point
print(style.BOLD + "\n\033[4m\033[1;33mTwinkle, twinkle, little star!\n" + style.END)

# you can see a continuation of the same codes here
print("\033[1;34mTwinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!\n")