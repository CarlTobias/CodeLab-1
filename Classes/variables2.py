# note: this file is rough notes...
# it may not be complete, or look messy, but this is just a preview of how i learn practically

# trying out valid variable names
from ctypes.wintypes import PINT


sentence = 'Today is 6th October, 2022, Thursday.'
sentence1 = 'Today is 6th October, 2022, Thursday.'
sentence_1 = 'Today is 6th October, 2022, Thursday.'
Sentence1 = 'Today is 6th October, 2022, Thursday.'
Sentence_1 = 'Today is 6th October, 2022, Thursday.'
SENTENCE1 = 'Today is 6th October, 2022, Thursday.'
SEnTEnCE1 = 'Today is 6th October, 2022, Thursday.'
SENTENCE_1 = 'Today is 6th October, 2022, Thursday.'
SEnTEnCE_1 = 'Today is 6th October, 2022, Thursday.'
_sentence = 'Today is 6th October, 2022, Thursday.'
today_date = 'Today is 6th October, 2022, Thursday.'
Today_Date = 'Today is 6th October, 2022, Thursday.'

print("\n", sentence, "\n", sentence1, "\n", sentence_1, "\n", Sentence1, "\n", Sentence_1,
      "\n", SENTENCE1, "\n", SEnTEnCE1, "\n", SENTENCE_1, "\n", SEnTEnCE_1, "\n",  _sentence, "\n", today_date, "\n", Today_Date)
# variable names that arent valid are the ones that start with numbers, -, *, or '

# trying different number variables (int, float, complex)

Alpha = 793520
beTa = 69.696969
_ChArLiE = 5j + 1

# using the "type" function to print the variable type

# type() is the funtion that is used to get the type of an object
print("\nThe type of Alpha is", type(Alpha), "\n")
print("The type of beTa is", type(beTa), "\n")
print("The type of _ChArLiE is", type(_ChArLiE), "\n")


# now, we're gonna use the input() funtion to get the user input

print("Enter Marks: ")

marks = int(input())

print("Marks obtained are", marks)

# okay, so let's try to get the area of a sqaure with user Input

length = float(input("What is the length of the side of your square: "))

Rarea = (length**2)

# so instead of using a comma, we are using + to reomve the unnecessary space that a comma gives in your printed sentenes
print("The area of your square is " + str(Rarea) + ".\n")

# now let's try getting the radius of a circle without importing pi from the system

pi = 3.14159265359

radius = float(input("What is the radius of your circle? "))

Carea = (pi*(radius**2))

# we'll apply the same steps that we used previously
print("The area of your circle is " + str(Carea) + ".\n")


# okay, we will try to play with string values

option1 = "Today is 6th October, 2022, Thursday."

print("\n" + option1 + "\n")
print(option1[0], "\n")
print(option1[0:5], "\n")
print(option1[4:], "\n")
print(option1*2, "\n")

option2 = "Today is our fifth session on 'Introduction to Programming.'"
print(option2, "\n")

option3 = "Today we are learning about different types of variables in Python Programming."
print(option3, "\n")

# if we want to keep sentences in one paragraph, we have to concatinate them by simply using the plus sign for every string...
# this is called "String Concatination"

print(option1 + " " + option2 + " " + option3 + "\n")

# if we want to change the cases of the variables, we can use different case syntaxes

shopping = "I want to go on a shopping spree!"

# to make lower case...
print(shopping.lower())

# to make upper case...
print(shopping.upper())

# to make every first letter of first word upper case...
print(shopping.title())

# to switch the cases of all existig characters in the string
print(shopping.swapcase())

# now, we're going to use the strip function... this allows us to remove the blank spaces in the string

bar = "\tA man walks into a bar.\n"

# this removes both blank spaces from left and rigth simultaneously
print("\n" + bar.strip())

# this removes only the leftmost blank space
print(bar.lstrip())

# this removes only the rightmost blank space
print(bar.rstrip())

# now to add a tab or newline we use \t or \n (respectively)

print("The programming language is \t Python.\n")
print("Programming Languages:\nPython\nC\nJavaScript\n")