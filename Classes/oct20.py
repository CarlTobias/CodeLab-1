# note: this file is rough notes...
# it may not be complete, or look messy, but this is just a preview of how i learn practically

# October 20, 2022

# Revision of if-else statements
num = int(input("\nGive a random integer: "))

if num > 0:
    print("This is a positive number.\n")
 

numb = int(input("\nGive me a number value for variable 'a': "))
er = int(input("\nGive me another number value for variable 'b': "))

# Another revision
if numb < er:
    print("\n" + str(er) + " is bigger in value compared to " + str(numb) + ".\n")

# more if-else statement revisions

print("Welcome to Nozama!")

website = str(input("Do you live in the United States or Austrailia? "))

if website.upper() == "united states" or website.upper() == "us" or website.upper() == "u.s." or website.upper() == "u.s":
    shipment = int(input("Shipment Amount: "))

    if shipment <= 50:
        print("Delivery charge is for $50.")
    
    else:
        print("Delivery charge is for $25.")

elif website.upper() == "austrailia":
    shipment = int(input("Shipment Amount: "))

    if shipment <= 100:
        print("Delivery charge is for $150.")

    else:
        print("Delivery charge is for $15.")


# activity: list-functions

flowers = ["dandelion", "sunflower", "buttercup"]
print((flowers))

flowers[2] = "rose"
print(flowers[0])
print(flowers[1])
print(flowers[2])

# .append adds an element to the end of the list
flowers.append("buttercup")
print(flowers)
# .insert adds to any place of your choice
flowers.insert(2, "rose")
print(flowers)

# .remove uses the data inside the quotation marks
flowers.remove("buttercup")
print(flowers)
# .pop removes the last element from the list
flowers.pop()
print(flowers)

# sort the list using .sort or .sort(reverse=True)
flowers.sort()
print(flowers)
flowers.sort(reverse=True)
print(flowers)

# to delete functions, we can use .del
del[flowers[0:5]]
print(flowers)

# dictionary function datatype

student = {"Name":"Carl Tobias", "I.D.":"2022-293", "Course":"Creative Computing"}

print(student)
print("Name: " + student["Name"])
print("I.D.: " + student["I.D."])
print("Course: " + student["Course"])

# chapter 5, exercise 1

personal_info = {"First Name":"Carl", "Last Name":"Tobias", "Age":"18", "City":"Dubai"}

print(personal_info)
print("First Name: " + personal_info["First Name"])
print("Last Name: " + personal_info["Last Name"])
print("Age: " + personal_info["Age"])
print("City: " + personal_info["City"])

# chapter 5, exercise 2

glossary = {
    "print" : "The print() function prints the specified message to the screen, or other standard output device.",
    "int" : "The int() function converts the specified value into an integer number.",
    "if-else" : "The if-else statement is used to execute both the true part and false part of a given condition."
}

print("print():\n  -" + glossary["print"])
print("print():\n  -" + glossary["int"])
print("print():\n  -" + glossary["if-else"])
