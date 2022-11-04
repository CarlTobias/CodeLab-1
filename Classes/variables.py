# note: this file is rough notes...
# it may not be complete, or look messy, but this is just a preview of how i learn practically

#in this lesson we're gonna learn how to use variables in python

"hello world"
'hello world'
'hello' ' ' 'world'
'hello' '-' 'world'
# hello world different syntaxes


'i love hamburgers more than spaghetti'
# i just wanted to say this lol

2
2+2
2+3*2
(2+3)*2

2398.340570239*23908518492/126817
500+60*28112/8-1
# trying different math equations

'2+2'
# adding quotes will be read as a sentence and not a mathematical expression

# numbers and words together

'hello'+'2'
'hello' * 2

# X=88, 89, 90, 65, 66
print('hi', ord('X'))
print(ord('Y'))
print(ord('Z'))
print(ord('A'))
print(ord('B'))

bin(4720938419280381097483)

from http.server import ThreadingHTTPServer


a = 89
bins = "trash"
cd, ef, gh = 23, 45, 78
Pi = 3.141592653589793

print("The product of Pi and the variable 'cd' is:", Pi*cd)
print(bins, "is synonymous to \"Garbage.\"")

#learning how to use the input function

name = input("Enter your name: ")
print("Your name is", name, ".")

#Taking input from user to calculate area of square

length = input("Enter the length of the square: ")

area = int(length)**2

print("The area of your square is:", area, ".")

#now we're using user defined functions to help us calculate area of a circle

from math import pi

r = float(input("Input the radius of the circle: "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi*r**2))

#now for rectangle

lengthr = input("Enter the length of the rectangle: ")
widthr = input("Enter the width of the rectangle: ")

arear = float(lengthr) * float(widthr)

print("The area of your rectangle is:", arear, ".")


print('\033[1;32;47mThe values of letters in Ordinary, Character, and Binary\n')
# the commands at the start of the first two print functions are there to help change the color of the text
print('\033[1;34;40mLtr', '\t', 'ord', '\tchr', '\tbin')

# we are gonna be printing each value of letter 'A' for ord, chr, and bin

# we print the letter first, then \t (tab function) to add a little space in between the texts
# the ord function is used as normal
# and we put the ord function inside the chr and bin function

print('A:', '\t', ord('A'), '\t', chr(ord('A')), '\t', bin(ord('A')))

# now we're doing it for the rest of the capital letters
print('B:', '\t', ord('B'), '\t', chr(ord('B')), '\t', bin(ord('B')))
print('C:', '\t', ord('C'), '\t', chr(ord('C')), '\t', bin(ord('C')))
print('D:', '\t', ord('D'), '\t', chr(ord('D')), '\t', bin(ord('D')))
print('E:', '\t', ord('E'), '\t', chr(ord('E')), '\t', bin(ord('E')))
print('F:', '\t', ord('F'), '\t', chr(ord('F')), '\t', bin(ord('F')))
print('G:', '\t', ord('G'), '\t', chr(ord('G')), '\t', bin(ord('G')))
print('H:', '\t', ord('H'), '\t', chr(ord('H')), '\t', bin(ord('H')))
print('I:', '\t', ord('I'), '\t', chr(ord('I')), '\t', bin(ord('I')))
print('J:', '\t', ord('J'), '\t', chr(ord('J')), '\t', bin(ord('J')))
print('K:', '\t', ord('K'), '\t', chr(ord('K')), '\t', bin(ord('K')))
print('L:', '\t', ord('L'), '\t', chr(ord('L')), '\t', bin(ord('L')))
print('M:', '\t', ord('M'), '\t', chr(ord('M')), '\t', bin(ord('M')))
print('N:', '\t', ord('N'), '\t', chr(ord('N')), '\t', bin(ord('N')))
print('O:', '\t', ord('O'), '\t', chr(ord('O')), '\t', bin(ord('O')))
print('P:', '\t', ord('P'), '\t', chr(ord('P')), '\t', bin(ord('P')))
print('Q:', '\t', ord('Q'), '\t', chr(ord('Q')), '\t', bin(ord('Q')))
print('R:', '\t', ord('R'), '\t', chr(ord('R')), '\t', bin(ord('R')))
print('S:', '\t', ord('S'), '\t', chr(ord('S')), '\t', bin(ord('S')))
print('T:', '\t', ord('T'), '\t', chr(ord('T')), '\t', bin(ord('T')))
print('U:', '\t', ord('U'), '\t', chr(ord('U')), '\t', bin(ord('U')))
print('V:', '\t', ord('V'), '\t', chr(ord('V')), '\t', bin(ord('V')))
print('W:', '\t', ord('W'), '\t', chr(ord('W')), '\t', bin(ord('W')))
print('X:', '\t', ord('X'), '\t', chr(ord('X')), '\t', bin(ord('X')))
print('Y:', '\t', ord('Y'), '\t', chr(ord('Y')), '\t', bin(ord('Y')))
print('Z:', '\t', ord('Z'), '\t', chr(ord('Z')), '\t', bin(ord('Z')))

# now we're doing for lowercase letters
print('a:', '\t', ord('a'), '\t', chr(ord('a')), '\t', bin(ord('a')))
print('b:', '\t', ord('b'), '\t', chr(ord('b')), '\t', bin(ord('b')))
print('c:', '\t', ord('c'), '\t', chr(ord('c')), '\t', bin(ord('c')))
print('d:', '\t', ord('d'), '\t', chr(ord('d')), '\t', bin(ord('d')))
print('e:', '\t', ord('e'), '\t', chr(ord('e')), '\t', bin(ord('e')))
print('f:', '\t', ord('f'), '\t', chr(ord('f')), '\t', bin(ord('f')))
print('g:', '\t', ord('g'), '\t', chr(ord('g')), '\t', bin(ord('g')))
print('h:', '\t', ord('h'), '\t', chr(ord('h')), '\t', bin(ord('h')))
print('i:', '\t', ord('i'), '\t', chr(ord('i')), '\t', bin(ord('i')))
print('j:', '\t', ord('j'), '\t', chr(ord('j')), '\t', bin(ord('j')))
print('k:', '\t', ord('k'), '\t', chr(ord('k')), '\t', bin(ord('k')))
print('l:', '\t', ord('l'), '\t', chr(ord('l')), '\t', bin(ord('l')))
print('m:', '\t', ord('m'), '\t', chr(ord('m')), '\t', bin(ord('m')))
print('n:', '\t', ord('n'), '\t', chr(ord('n')), '\t', bin(ord('n')))
print('o:', '\t', ord('o'), '\t', chr(ord('o')), '\t', bin(ord('o')))
print('p:', '\t', ord('p'), '\t', chr(ord('p')), '\t', bin(ord('p')))
print('q:', '\t', ord('q'), '\t', chr(ord('q')), '\t', bin(ord('q')))
print('r:', '\t', ord('r'), '\t', chr(ord('r')), '\t', bin(ord('r')))
print('s:', '\t', ord('s'), '\t', chr(ord('s')), '\t', bin(ord('s')))
print('t:', '\t', ord('t'), '\t', chr(ord('t')), '\t', bin(ord('t')))
print('u:', '\t', ord('u'), '\t', chr(ord('u')), '\t', bin(ord('u')))
print('v:', '\t', ord('v'), '\t', chr(ord('v')), '\t', bin(ord('v')))
print('w:', '\t', ord('w'), '\t', chr(ord('w')), '\t', bin(ord('w')))
print('x:', '\t', ord('x'), '\t', chr(ord('x')), '\t', bin(ord('x')))
print('y:', '\t', ord('y'), '\t', chr(ord('y')), '\t', bin(ord('y')))
print('z:', '\t', ord('z'), '\t', chr(ord('z')), '\t', bin(ord('z')))

# AND I... THANK... YOU.

# program made by Carl
