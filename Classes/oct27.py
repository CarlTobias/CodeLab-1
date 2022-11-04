# note: this file is rough notes...
# it may not be complete, or look messy, but this is just a preview of how i learn practically

# today we will be learning about loops!!!!!!!!

# while loops will run until the statement becomes true

count = 0 # here, we state a variable and its value
while count <= 10: # this basically says "the program will continue as long as count is equal to and only equal to 10"
    # this will be the instructions that the while loop will be following
    print(count)
    count = count + 1

favplace = []
counter = 0

while True:
    counter = counter + 1
    places = input("What is your most favourite place? ")
    favplace.append(places.title())
    placess = input("What is your second most favourite place? ")
    favplace.append(placess.title())
    placesss = input("What is your third most favourite place? ")
    favplace.append(placesss.title())
    if counter == 3:
      print("My top 3 favourite places to go to are:\n-" + str(favplace[0]) + "\n-" + str(favplace[1]) + "\n-" + str(favplace[2]))
      break

#activity 4

trees = ["Oak", "Birch", "Sycamore", "Elm"]

for trees in trees:
    print(trees)

student = {"Name":input()}

# try it yourself lol

sandwich_orders = ["Veggie", "Grilled Cheese", "Turkey", "Tuna", "Ham and Cheese", "Nutella", "Peanut Butter"]
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwich.append(current_sandwich)

print("\n")
print("Sandwich Orders: ")
for sandwich in finished_sandwich:
    print(sandwich + " Sandwich")

#functionss (start of chapter 7)

