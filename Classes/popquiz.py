# create a restaurant menu using dictionary
# order each item separately
# for every time an order is made, print a new menu excluding the item that was ordered

print("\nWelcome to Ristorante di Carlo!\n")

menu = {"Starter": ["Bruschetta", "Caponata", "Crostini", "Focaccia", "Italian Meatballs"],
        "Pizza": ["Bianca", "Caprese", "Capricciosa", "Margherita", "Marinara", "Napoletana", "Pizzette"],
        "Pasta" : ["Cacio e Pepe", "Carbonara", "Fettuccine Alfredo", "Gnocchi", "Lasagne", "Pesto", "Ravioli"],
        "Dessert" : ["Basic Biscotti", "Chocolate Chip Biscotti", "Strawberry Gelato", "Vanilla Gelato", "Panna Cotta", "Tiramisu"]}
finished_order = []

print("-------------------- " * 6)
print("\nMenu:\n")
for keys, values in menu.items():
    print(str(keys) + ": " + str(values))

print("\n")

orderup_starter = input("What starter would you like to order? ")

while True:
    if orderup_starter.upper() == "DONE":
        break

    elif orderup_starter.title() in menu["Starter"]:
        menu["Starter"].remove(orderup_starter)
        finished_order.append(orderup_starter)
    
    else:
        print("That item is not on the menu. Please try again.")

print("\n-------------------- " * 6)
print("\nMenu:\n")
for keys, values in menu.items():
    print(str(keys) + ": " + str(values))

orderup_maincourse = input("What would be your main dish order? ")

while True:
    if orderup_maincourse.upper() == "DONE":
        break

    elif orderup_maincourse.title() in menu["Pizza"] or orderup_maincourse.title() in menu["Pizza"]:
        menu["Starter"].remove(orderup_maincourse)
        finished_order.append(orderup_maincourse)

    else:
        print("That item is not on the menu. Please try again.")

print("\n-------------------- " * 6)
print("\nMenu:\n")
for keys, values in menu.items():
    print(str(keys) + ": " + str(values))

orderup_dessert = input("And finally, what would you like for dessert? ")

while True:
    if orderup_maincourse.upper() == "DONE":
        break

    elif orderup_dessert.title() in menu["Dessert"]:
        menu["Starter"].remove(orderup_dessert)
        finished_order.append(orderup_dessert)

    else:
        print("That item is not on the menu. Please try again.")

print("We are all sold out for today!\nThank you very much for coming!\n")