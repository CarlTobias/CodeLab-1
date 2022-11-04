# note: this file is rough notes...
# it may not be complete, or look messy, but this is just a preview of how i learn practically

# we are gonna use the "in" and "not in" operators

print("\n")

a = 24
b = 10
list = [10, 20, 30, 40]

if (a not in list):
    print("a is not present in given list")

else:
    print("a is present in given list")

if (b in list):
    print("b is present in given list")

else:
    print("b is not present in given list")

print("\n\n")

# try ourselves

friends = ["iashlayne", "kristian", "rafael", "patricia", "ysabelle", "krunch", "renzie"]

print("Heeeeyyy, " + friends[0].title() + "!")
print("Halloooo, " + friends[1].title() + "!")
print("Holaaa, " + friends[2].title() + "!")
print("Bonjourr, " + friends[3].title() + "!")
print("Hi, " + friends[4].title() + "!")
print("Allo, " + friends[5].title() + "!\n'\n")

# to modify an element in the list, just simply identify the item in the list and input a new value

snacks = ["milky way", "kitkat", "maltesers"]

print("My favourite chocolate snacks:")
snacks = [each_string.title() for each_string in snacks]
str(print(*snacks, sep = ", "))
print("\n")

snacks[1] = "kinder"

print("My favourite chocolate snacks:")
str(print(*snacks, sep = ", "))
print("\n")

# to insert, use "list".insert[(insert a number)]

snacks = ["milky way", "kitkat", "maltesers"]

snacks = [each_string.title() for each_string in snacks]
print("My favourite chocolate snacks:")
str(print(*snacks, sep = ", "))
print("\n")

snacks.insert(0, "kinder")
snacks.insert(3, "dairy milk")
snacks.insert(1, "toblerone")

# the extra commands here let us print the whole list while capitalizing them so that we dont have to individually input them

snacks = [each_string.title() for each_string in snacks]
print("My favourite chocolate snacks:")
str(print(*snacks, sep = ", "))
print("\n")
