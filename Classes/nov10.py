# tuples!!!

# Program Activity 1

# here we defined two tuples "fruits" and "vegetables"
fruits = ("apple", "orange", "grape")
vegetables = ("broccoli", "carrot", "potato")

# we access the elements of the tuples using index individually here
print("\nFruit Index:")
print(fruits.index("apple"))
print(fruits.index("orange"))
print(fruits.index("grape"))

print("\Vegetable Index:")
print(vegetables.index("broccoli"))
print(vegetables.index("carrot"))
print(vegetables.index("potato"))

print("\n" + str(fruits[0]))
print(fruits[1])
print(fruits[2])
print(vegetables[0])
print(vegetables[1])
print(str(vegetables[2]) + "\n")

# and here, we print the elements of the tuple together
print("Fruits:\n" + str(fruits[0:3]) + "\n")
print("Vegetables:\n" + str(vegetables[0:3]) + "\n")

# now here, we use a "for" loop to access the elements of the tuple
print("Fruits:\n")
for f in fruits:
    print(f)

for v in vegetables:
    print(v)


# Program Activity 2

# here, we see tuples with years (leap and non-leap)
leapyrs = (2032, 2020, 2028, 2024)
nleapyrs = (2021, 2003, 2015, 2030)

# here, i printed leap and non-leap years and concatenated with some text too
print("Leap Years:\n" + str(leapyrs[0:4]) + "\n")
print("Non-Leap Years:\n" + str(nleapyrs[0:4]) + "\n")

# i multiplied each element by 3 for leap...
print("Leap Years * 3: ")
print(str(int(leapyrs[0]) * 3) + "\n")
print(str(int(leapyrs[1]) * 3) + "\n")
print(str(int(leapyrs[2]) * 3) + "\n")
print(str(int(leapyrs[3]) * 3) + "\n")

# and non-leap years
print("Non-Leap Years * 3: ")
print(str(int(nleapyrs[0]) * 3) + "\n")
print(str(int(nleapyrs[1]) * 3) + "\n")
print(str(int(nleapyrs[2]) * 3) + "\n")
print(str(int(nleapyrs[3]) * 3) + "\n")

# here, i used an if-else statement to compare tuple elements with each other
if leapyrs[3] > nleapyrs[1]:
    print("True\n")

else:
    print("False\n")

# i used "len()" to print the length of each tuple
print("Length of Tuples:\n")
print(len(leapyrs), "\n")
print(len(nleapyrs), "\n")

# i used "sum()" to print the sum of each tuple
print("Sum of Tuples:\n")
print(sum(leapyrs), "\n")
print(sum(nleapyrs), "\n")

# i used "sorted()" to print each tuple sorted (without modifying the tuple)
print("Sorted Tuples:\n")
print(sorted(leapyrs), "\n")
print(sorted(nleapyrs), "\n")

# i swapped the tupples and printed them
print("Swapping of Tuples:\n")
nleapyrs, leapyrs = leapyrs, nleapyrs
print(leapyrs, "\n")
print(nleapyrs, "\n")
