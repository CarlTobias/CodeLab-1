# for this assessment, i will be making a program simulating the experience of using a vending machine

# initially, i add this to enable me to bolden texts later on

bold = "\33[1m"
normal = "\33[m"

# then, i start by creating a dictionary with all the items i want the vending machine to vend

# here i made a list of all the items (for ease on later codes)
menumenu = {"A1" : ["Lay's (Original)", "AED 2.50"], "A2" : ["Lay's (Tomato Ketchup)", "AED 2.50"], "A3" : ["Lay's (Salt & Vinegar)", "AED 2.50"], "A4" : ["Forno (Authentic Cheese)", "AED 3.50"],
            "B1" : ["Pringles (Original)", "AED 4.50"], "B2" : ["Pringles (Sour Cream & Onion)", "AED 4.50"], "B3" : ["Stix (Slightly Salted)", "AED 3.00"], "B4" : ["Stix (Tomato Ketchup)", "AED 3.00"],
            "C1" : ["L'uisine (Plain Croissant)", "AED 1.00"], "C2" : ["L'uisine (Cheese Croissant)", "AED 1.50"], "C3" : ["L'uisine (Cheese Puff)", "AED 2.50"], "C4" : ["7Days (Chocolate Croissant)", "AED 1.00"],
            "D1" : ["Coca Cola", "AED 2.50"], "D2" : ["Coca Cola (Light)", "AED 2.00"], "D3" : ["Pepsi", "AED 2.50"], "D4" : ["Pepsi (Diet)", "AED 2.00"],
            "E1" : ["Sprite", "AED 2.50"], "E2" : ["Fanta", "AED 2.50"], "E3" : ["Water (Mai Dubai)", "AED 1.50"], "E4" : ["Water (Al Ain)", "AED 1.50"],
            "F1" : ["Capri-Sun (Apple)", "AED 2.20"], "F2" : ["Capri-Sun (Orange)", "AED 2.20"], "F3" : ["Capri-Sun (Strawberry)", "AED 2.20"], "F4" : ["Capri-Sun (Tropical)", "AED 2.20"],
            "G1" : ["Baskin Robbins 120ml (Vanilla)", "AED 6.40"], "G2" : ["Baskin Robbins 120ml (Chocolate)", "AED 6.40"], "G3" : ["Baskin Robbins 120ml (Praline Delight)", "AED 6.40"], "G4" : ["Baskin Robbins 120ml (Cotton Candy)", "AED 6.40"],
            "H1" : ["Chocolate Chip Brownie", "AED 3.50"], "H2" : ["Oreos", "AED 2.00"], "H3" : ["Oreos (Golden)", "AED 2.00"], "H4" : ["Choco Cookies", "AED 1.50"],
            "I1" : ["Chocapic", "AED 3.15"], "I2" : ["Cinnamon Toast Crunch", "AED 5.00"], "I3" : ["Lacnor (Skimmed Milk 150ml)", "AED 2.50"], "I4" : ["Alpro (Almond Milk 150ml)", "AED 4.00"]}

menu1 = {"A1" : "Lay's (Original)", "A2" : "Lay's (Tomato Ketchup)", "A3" : "Lay's (Salt & Vinegar)", "A4" : "Forno (Authentic Cheese)",
         "B1" : "Pringles (Original)", "B2" : "Pringles (Sour Cream & Onion)", "B3" : "Stix (Slightly Salted)", "B4" : "Stix (Tomato Ketchup)",
         "C1" : "L'uisine (Plain Croissant)", "C2" : "L'uisine (Cheese Croissant)", "C3" : "L'uisine (Cheese Puff)", "C4" : "7Days (Chocolate Croissant)",
         "D1" : "Coca Cola", "D2" : "Coca Cola (Light)", "D3" : "Pepsi", "D4" : "Pepsi (Diet)",
         "E1" : "Sprite", "E2" : "Fanta", "E3" : "Water (Mai Dubai)", "E4" : "Water (Al Ain)",
         "F1" : "Capri-Sun (Apple)", "F2" : "Capri-Sun (Orange)", "F3" : "Capri-Sun (Strawberry)", "F4" : "Capri-Sun (Tropical)",
         "G1" : "Baskin Robbins 120ml (Vanilla)", "G2" : "Baskin Robbins 120ml (Chocolate)", "G3" : "Baskin Robbins 120ml (Praline Delight)", "G4" : "Baskin Robbins 120ml (Cotton Candy)",
         "H1" : "Chocolate Chip Brownie", "H2" : "Oreos", "H3" : "Oreos (Golden)", "H4" : "Choco Cookies",
         "I1" : "Chocapic", "I2" : "Cinnamon Toast Crunch", "I3" : "Lacnor (Skimmed Milk 150ml)", "I4" : "Alpro (Almond Milk 150ml)"}

# and here i made another dictionary of the same thing as the one above, but this time it's the code and price
menumenuprice = {"A1" : 2.50, "A2" : 2.50, "A3" : 2.50, "A4" : 3.50,
                 "B1" : 4.50, "B2" : 4.50, "B3" : 3.00, "B4" : 3.00,
                 "C1" : 1.00, "C2" : 1.50, "C3" : 2.50, "C4" : 1.00,
                 "D1" : 2.50, "D2" : 2.00, "D3" : 2.50, "D4" : 2.00,
                 "E1" : 2.50, "E2" : 2.50, "E3" : 1.50, "E4" : 1.50,
                 "F1" : 2.20, "F2" : 2.20, "F3" : 2.20, "F4" : 2.20,
                 "G1" : 6.40, "G2" : 6.40, "G3" : 6.40, "G4" : 6.40,
                 "H1" : 3.50, "H2" : 2.00, "H3" : 2.00, "H4" : 1.50,
                 "I1" : 3.15, "I2" : 5.00, "I3" : 2.50, "I4" : 4.00}

# this dictionary is only for printing the snacks option
food = {f"{bold}A1{normal}" : ["Lay's (Original)", "AED 2.50"], f"{bold}A2{normal}" : ["Lay's (Tomato Ketchup)", "AED 2.50"], f"{bold}A3{normal}" : ["Lay's (Salt & Vinegar)", "AED 2.50"], f"{bold}A4{normal}" : ["Forno (Authentic Cheese)", "AED 3.50"], 
        f"{bold}B1{normal}" : ["Pringles (Original)", "AED 4.50"], f"{bold}B2{normal}" : ["Pringles (Sour Cream & Onion)", "AED 4.50"], f"{bold}B3{normal}" : ["Stix (Slightly Salted)", "AED 3.00"], f"{bold}B4{normal}" : ["Stix (Tomato Ketchup)", "AED 3.00"], 
        f"{bold}C1{normal}" : ["L'uisine (Plain Croissant)", "AED 1.00"], f"{bold}C2{normal}" : ["L'uisine (Cheese Croissant)", "AED 1.50"], f"{bold}C3{normal}" : ["L'uisine (Cheese Puff)", "AED 2.50"], f"{bold}C4{normal}" : ["7Days (Chocolate Croissant)", "AED 1.00"]}

# and again, like the other one, this dictionary is where i will be keeping the price to be able to calculate it later on
foodprice = {"A1" : 2.50, "A2" : 2.50, "A3" : 2.50, "A4" : 3.50,
             "B1" : 4.50, "B2" : 4.50, "B3" : 3.00, "B4" : 3.00,
             "C1" : 1.00, "C2" : 1.50, "C3" : 2.50, "C4" : 1.00}

# this is for drinks
drinks = {f"{bold}D1{normal}" : ["Coca Cola", "AED 2.50"], f"{bold}D2{normal}" : ["Coca Cola (Light)", "AED 2.00"], f"{bold}D3{normal}" : ["Pepsi", "AED 2.50"], f"{bold}D4{normal}" : ["Pepsi (Diet)", "AED 2.00"],
          f"{bold}E1{normal}" : ["Sprite", "AED 2.50"], f"{bold}E2{normal}" : ["Fanta", "AED 2.50"], f"{bold}E3{normal}" : ["Water (Mai Dubai)", "AED 1.50"], f"{bold}E4{normal}" : ["Water (Al Ain)", "AED 1.50"],
          f"{bold}F1{normal}" : ["Capri-Sun (Apple)", "AED 2.20"], f"{bold}F2{normal}" : ["Capri-Sun (Orange)", "AED 2.20"], f"{bold}F3{normal}" : ["Capri-Sun (Strawberry)", "AED 2.20"], f"{bold}F4{normal}" : ["Capri-Sun (Tropical)", "AED 2.20"]}

drinksprice = {"D1" : 2.50, "D2" : 2.00, "D3" : 2.50, "D4" : 2.00,
               "E1" : 2.50, "E2" : 2.50, "E3" : 1.50, "E4" : 1.50,
               "F1" : 2.20, "F2" : 2.20, "F3" : 2.20, "F4" : 2.20}

# this is for extras like dessert
extras = {f"{bold}G1{normal}" : ["Baskin Robbins 120ml (Vanilla)", "AED 6.40"], f"{bold}G2{normal}" : ["Baskin Robbins 120ml (Chocolate)", "AED 6.40"], f"{bold}G3{normal}" : ["Baskin Robbins 120ml (Praline Delight)", "AED 6.40"], f"{bold}G4{normal}" : ["Baskin Robbins 120ml (Cotton Candy)", "AED 6.40"],
          f"{bold}H1{normal}" : ["Chocolate Chip Brownie", "AED 3.50"], f"{bold}H2{normal}" : ["Oreos", "AED 2.00"], f"{bold}H3{normal}" : ["Oreos (Golden)", "AED 2.00"], f"{bold}H4{normal}" : ["Choco Cookies", "AED 1.50"], 
          f"{bold}I1{normal}" : ["Chocapic", "AED 3.15"], f"{bold}I2{normal}" : ["Cinnamon Toast Crunch", "AED 5.00"], f"{bold}I3{normal}" : ["Lacnor (Skimmed Milk 150ml)", "AED 2.50"], f"{bold}I4{normal}" : ["Alpro (Almond Milk 150ml)", "AED 4.00"]}

extrasprice = {"G1" : 6.40, "G2" : 6.40, "G3" : 6.40, "G4" : 6.40,
               "H1" : 3.50, "H2" : 2.00, "H3" : 2.00, "H4" : 1.50,
               "I1" : 3.15, "I2" : 5.00, "I3" : 2.50, "I4" : 4.00}

# and finally, we have a dictionary for combos
# i made this to give the user a chance to make a quicker purchase
combos = {f"Breakfast Club - {bold}BC1{normal}" : ["Cinnamon Toast Crunch & Lacnor Skimmed Milk", "AED 7.50"], f"Breakfast Club (Lactose Free) - {bold}BC2{normal}" : ["Cinnamon Toast Crunch & Alpro Almond Milk", "AED 9.00"],
          f"Lay's Lover - {bold}CH1{normal}" : ["All Lay's Flavours (Excluding Forno) & Coca Cola", "AED 10.00"], f"Pringles Heaven - {bold}CH2{normal}" : ["All Pringle Flavours & Any Drink of Your Choice", "AED 11.50"],
          f"Snack Pack 1 - {bold}AI1{normal}" : ["Forno (Authentic Cheese), Stix (Slightly Salted), & Water (Mai Dubai)", "AED 8.00"], f"Snack Pack 2 - {bold}AI2{normal}" : ["Lay's (Original), Pringles (Original), & Water (Mai Dubai)", "AED 8.50"],
          f"Brain Freeze 1 - {bold}BF1{normal}" : ["Baskin Robbins (Chocolate) & Oreos", "AED 8.40"], f"Brain Freeze 2 - {bold}BF2{normal}" : ["Baskin Robbins (Vanilla) & Cinnamon Toast Crunch", "AED 11.40"]}

combos1 = {"BC1" : "Breakfast Club Combo", "BC2" : "Lactose Free Breakfast Club Combo",
          "CH1" : "Lay's Lover Combo", "CH2" : "Pringles Heaven Combo",
          "AI1" : "Snack Pack Combo 1", "AI2" : "Snack Pack Combo 2",
          "BF1" : "Brain Freeze Combo 1", "BF2" : "Brain Freeze Combo 2"}

combosprice = {"BC1" : 7.50, "BC2" : 9.00,
               "CH1" : 10.00, "CH2" : 11.50,
               "AI1" : 8.00, "AI2" : 8.50,
               "BF1" : 8.40, "BF2" : 11.40}


# here i define my own function in order to keep my code shorter and as concise as can be

# this one is for printing the menu
def menu():
    print(f"{bold}Snacks:{normal}")
    for AnBnC, one2four1 in food.items():
        print(str(AnBnC) + " - " + str(one2four1))

    print("\n")
    print(f"{bold}Drinks:{normal}")
    for DnEnF, one2four2 in drinks.items():
        print(str(DnEnF) + " - " + str(one2four2))

    print("\n")
    print(f"{bold}Extras:{normal}")
    for GnHnI, one2four3 in extras.items():
        print(str(GnHnI) + " - " + str(one2four3))

    
    

# here, i defined a variable for the final price and where the user can input the money to pay
totalprice = 0
totalmoney = 0

# here, i also have a list where i can append (add) all the items the user will buy so i can then show it later on
itemsbought = []


# here is a welcoming line
print(f"\n{bold}Welcome to Vendimus Prime!{normal}\n\n")

# and the menu is immediately printed
print(f"{bold}Menu:{normal}\n")
menu()

# i have the program set to ask the user first if they wanted to buy a combo for a faster purchase
print("\n\nDo you want to purchase one of our combos for a quick purchase?")
# here i put input for their choice
quickies = input(f"Enter '{bold}A{normal}' for Yes or '{bold}B{normal}' for No: ").upper()

# this if-else statement makes the choice on which block of code to run
if quickies == "A":
    # if the user inputs "A," then the program will print the list of the combos
    print("Combos:\n")
    for com, bos in combos.items():
        print(str(com) + " - " + str(bos))
    
    # and after that, i made a while statement that asks for another input for the combo code
    run = True
    while run:
        print("\n\nWhat combo would you like to purchase?")
        print(f"If none, enter '{bold}B{normal}'\n")
        comboinput = input("Please enter the corresponding code for the combo: ").upper()

        # inside the while loop, there is another if-else statement
        if comboinput == "B":
            # if the user inputs "B," the program will break the while loop and continue the program
            # this will lead straight to the manual purchase section
            print("Okay.\n")
            break
        
        elif comboinput in combosprice:
            # otherwise, it will ask the user again just to make sure that they are satisfied with their input
            run2 = True
            while run:
                print(f"You chose {comboinput}.\n")
                print("Is that right?")
                # i used the defined function i made earlier
                right = input("Enter 'A' for Yes or 'B' for No: ").upper()
                
                if right == "A":
                    # if the input is "A," program will follow the following block:
                    print(f"\n{bold}Great!{normal}\n")
                    totalprice += combosprice[comboinput]
                    itemsbought.append(combos1[comboinput])
                    break
                    
                # if the input is "B," the program will print the menu for combos once more and repeat the loop
                elif right == "B":
                    print("Combos:\n")
                    for com, bos in combos.items():
                        print(str(com) + " - " + str(bos))
                        break
                
                # otherwise, the program will print "Invalid input" and tell the user to try again
                else:
                    print("Invalid input. Try Again.\n")
            run2 = False
        
        # if the input is anything else other than "B" or anything in the combo list (similar to the code inside the nested while loop),
        # the program will print "Invalid input" and repeat the loop
        else:
            print("Invalid input. Please try again.\n")
        run = False
    
        # after the if-else statement, the program would then move on to the next part
        # i made it so that the program would ask if the user would want anything else to add to the combo
        # (to make it more user-friendly)
        
           

# now, if the user wants to purchase individual items, they would have to enter "B" (according to this elif statement)
elif quickies == "B":
    # inside, the menu for "snacks" is printed using a for loop
    print("\n\n\n\n\nO-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O\n\n\n\n\n")
    print(f"{bold}Snacks:{normal}")
    for AnBnC, one2four1 in food.items():
        print(str(AnBnC) + " - " + str(one2four1))
    
    # after that, a while loop is used yet again
    # this loop is similar to the one earlier (found in the combos part)    
    run = True
    while run:
        # in the loop. the program will ask for what snack the user wants
        print("\n\nWhat would you like to purchase for snacks?")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose1 = input("Enter a code: ").upper()

        # and this if-else statement is used for the user input above
        if choose1 == "B":
            # if the user enters "B," the program will proceed to print the following:
            print("Okay.\n")
            # and break the loop
            break
        
        # and if the input is inside the dictionary for the snacks, this block will run
        elif choose1 in foodprice:
            run2 = True
            while run2:
                # now, like the other previous while loops, this acts as a failsafe to make a more user-friendly program
                # it asks the user if their initial input is correct
                print(f"You chose {bold}{choose1}{normal}.\n")
                print("Is that right?")
                right = input("Enter 'A' for Yes or 'B' for No: ").upper()
                
                if right == "A":
                    # if it is, then the program will say "Great!" and add the price to their total bill
                    print(f"\n{bold}Great!{normal}\n")
                    totalprice += foodprice[choose1]
                    itemsbought.append(menu1[choose1])
                    run = False
                    run2 = False
                
                elif right == "B":
                    # and if the input is wrong, the menu for snacks will print and the loop will repeat
                    print(f"{bold}Snacks:{normal}")
                    for AnBnC, one2four1 in food.items():
                        print(str(AnBnC) + " - " + str(one2four1))
                    run2 = False
                    
                else:
                    # if the input is neither "A" or "B," then the program will print the following:
                    print("Invalid input. Try Again.\n")
                    # and it will run the while loop again (essentially forever until the user inputs correctly)

        
        # and this else statement prints invalid input, so that the user will have the opportunity to input the correct code
        # same as the code just above this one
        else:
            print("Invalid input. Please try again.\n")
        
    
        
    # this next part is the exact same code block as the one above, but is made for the "drinks" section
    print(f"{bold}Drinks:{normal}")
    for DnEnF, one2four2 in drinks.items():
        print(str(DnEnF) + " - " + str(one2four2))
        
    run3 = True
    while run3:
        print("\n\nWhat would you like to purchase for drinks?")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose2 = input("Enter a code: ").upper()

        if choose2 == "B":
            print("Okay.\n")
            break

        elif choose2 in drinksprice:
            run4 = True
            while run4:
                print(f"You chose {bold}{choose2}{normal}.\n")
                print("Is that right?")
                right = input("Enter 'A' for Yes or 'B' for No: ").upper()
                
                if right == "A":
                    print(f"\n{bold}Great!{normal}\n")
                    totalprice += drinksprice[choose2]
                    itemsbought.append(menu1[choose2])
                    run3 = False
                    run4 = False
                
                elif right == "B":
                    print(f"{bold}Drinks:{normal}")
                    for DnEnF, one2four2 in food.items():
                        print(str(DnEnF) + " - " + str(one2four2))
                    run4 = False
                    
                else:
                    print("Invalid input. Try Again.\n")

        else:
            print("Invalid input. Please try again.\n")
    
    
        
    # and this next part is the exact same code block again, but is made for the "extras" section
    print(f"{bold}Extras:{normal}")
    for GnHnI, one2four3 in extras.items():
        print(str(GnHnI) + " - " + str(one2four3))
        
    run5 = True
    while run5:
        print("\n\nWhat would you like to purchase any extras?")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose3 = input("Enter a code: ").upper()
    
        if choose3 == "B":
            print("Okay.\n")
            break
        
        elif choose3 in extrasprice:
            run6 = True
            while run6:
                print(f"You chose {bold}{choose3}{normal}.\n")
                print("Is that right?")
                right = input("Enter 'A' for Yes or 'B' for No: ").upper()
                
                if right == "A":
                    print(f"\n{bold}Great!{normal}\n")
                    totalprice += extrasprice[choose3]
                    itemsbought.append(menu1[choose3])
                    run5 = False
                    run6 = False
                    
                elif right == "B":
                    print(f"{bold}Extras:{normal}")
                    for GnHnI, one2four3 in extras.items():
                        print(str(GnHnI) + " - " + str(one2four3))
                    run6 = False
                
                else:
                    print("Invalid input. Try Again.\n")
        
        else:
            print("Invalid input. Please try again.\n")


# inside this triple nested while loop is a set of codes that deals with the chance that the user wants to add something to their "cart"
addrun1 = True
while addrun1:

    print("Would you like to add something else?")
    anyother = input("Enter 'A' for Yes or 'B' for No: ").upper()
            
    if anyother == "A":
    # if input is equal to "A," the following code will be followed:
                    
        # the menu is printed again
        menu()
                        
        # and inside this nested while loop are commands that have been used and explained previously
        addrun2 = True
        while addrun2:
        
            print("\nWhat would you like to add?")
            add = input("Please enter a code: ").upper()
            
            if add in menumenuprice:
                print(f"You chose {menumenu[add]}\n")
                
                addrun3 = True        
                while addrun3:
                    print("Is that right?")
                    right = input("Enter 'A' for Yes or 'B' for No: ").upper()
                        
                    if right == "A":
                        print("\nOkay. Moving on.\n")
                        totalprice += menumenuprice[add]
                        addrun2 = False
                        addrun3 = False
                            
                    elif right == "B":
                        print("Please view the menu again.\n")
                        addrun3 = False
                            
                    else:
                        print("Invalid input. Try Again.\n")
                    
            # i used another if-else statement for the decision    
            elif anyother == "B":
                print("Alright! Moving On.")
                addrun1 = False
                addrun2 = False
            
            else:
                print("Invalid input. Try again.\n")
    
    elif anyother == "B":
        print("Alright. Moving on.")
        addrun1 = False
    
    else:
        print("Invalid input. Try again\n")


print("\n\n\n\n\nO-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O-O\n\n\n\n\n")

# finally, the program will thank the user for using the program
print("Thank you for using Vendimus Prime!\n")

# and shows the user's total bill  
print(f"Your total is {bold}AED {totalprice}{normal}.")
# it tells the user to insert money to receive the items ordered
print("\nTo purchase, please insert money.\n")

# these three lines inform the user of the useable bills and coins,
# and it also informs the user that the minimum amount to be able to purchase anything is 3 dhs
print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
print("All coins are accepted.\n")
print(f"The minimum amount is {bold}AED 3{normal}")

        
money = (float(input("\nPlease insert here: ")))
# it will be added to a variable named totalmoney
totalmoney += money

# now... i added a totalmoney variable to allow the user to input smaller bills
# with this, the user can install money little by little until the amount of money added is greater than or equal to the bill
# (to simulate real-world situations)

# this while loop takes care of that
while money < totalprice:
    # first, it prints the following and asks the user to input more money
    print(f"Almost there! Just {bold}AED {totalprice - totalmoney}{normal} left.")
    money = (float(input("\nPlease insert here: ")))
    totalmoney += money
    
    if totalmoney >= totalprice:
        # once the total of all the money (inputted by the user) is greater than or equal to the bill,
        # then the text below will be printed;
        print(f"\nGreat! You inserted a total of {bold}AED {totalmoney}{normal}.")
        # and the loop will break
        break
    
    # and this else statement is what is followed when the money inserted is invalid    
    else:
        # i had the program ask the user again for money input (for the user's convenience)
        print(f"\n{bold}Invalid bill/s or coin/s.{normal}")
        print("Please try again.\n")
            
        print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
        print("All coins are accepted.\n")
        print(f"The minimum amount is {bold}AED 3{normal}")
            
        money = (float(input("\nPlease insert here: ")))
        totalmoney += money
            
        # i also inputted the same loop as earlier
        while totalmoney < totalprice:
            print(f"Almost there! Just AED {totalprice - money} left.")
            money = (float(input("\nPlease insert here: ")))
            totalmoney += money
            


# now, if the user's total bill is greater than 20, i will be offering a free item from the "extras" section
if totalprice > 20:
    # here is the text congratulating the user and informing them of what's happening
    print(f"Congratulations! You've made a purchase higher than {bold}AED 20{normal}.")
    print("Because of that, please choose any additional item from 'Extras'")
    print(f"{bold}Free of charge!{normal}")
    
    # this is where the process of that happens
    # the extrasmenu is printed
    print(f"{bold}Extras:{normal}")
    for GnHnI, one2four3 in extras.items():
        print(str(GnHnI) + " - " + str(one2four3))
    
    # and a while loop is used to help with the user's input like before
    run7 = True
    while run7:
        print("\n\nPLease pick an extra item.")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose4 = input("Enter a code: ").upper()
    
        if choose4 == "B":
            # if the user does not want to take a free item, the program will continue
            print("Okay.\n")
            break
        
        elif choose4 in extrasprice:
            # if the user wants to avail the free item of their choice,
            # another while loop is used to help with reassuring the user's choice
            run8 = True
            while run8:
                print(f"You chose {bold}{choose4}{normal}.\n")
                print("Is that right?")
                right = input("Enter 'A' for Yes or 'B' for No: ").upper()
                
                if right == "A":
                    print("\nGreat!\n")
                    itemsbought.append(menu1[choose4])
                    # you'll notice here that i did not include the code that adds to the total bill;
                    # and that's because, this item is free
                
                    run7 = False
                    run8 = False
                    
                elif right == "B":
                    # this is to make sure that the user a chance to change their choice
                    print("Extras:")
                    for GnHnI, one2four3 in extras.items():
                        print(str(GnHnI) + " - " + str(one2four3))
                    run8 = False
                
                else:
                    # if it's anything that is not on the menu, this will print
                    print("Invalid input. Try Again.\n")
        
        else:
            # same goes for this part
            print("Invalid input. Please try again.\n")
    
        
print(f"\n{bold}Vending...{normal}\n")

# here, i print the items that the user bought to let them know which items are being vended
print(f"Items being received are:")

for items in itemsbought:
    print(f"- {bold}{items}{normal}")

print("\n")

# the final part of the program starts here
# first, i made a formula to calculate the change
change =  totalmoney - totalprice

# now, if change is 0, the user will not receive change
if change <= 0:
    # instead, the user will receive this message
    print("You have no change.\n")
    print("Come again soon. Thank you!\n")

# if the user has change that isn't 0.25, 0.50, or 0.75, then the program will follow this block
elif change <= 0.24 or change > 0.49 <= 0.26 or change > 0.74 <= 0.51 or change > 0.99 <= 0.76:
    # the user will still have no change because it is impossible to give change for it
    print("You have no change.\n")
    print("Come again soon. Thank you!\n")

# otherwise, the user will be getting the message below
else:
    # the total change will be shown
    print(f"Your change is {bold}AED {change}{normal}\n")
    
    # then the program will ask if the user would like to receive it or to donate it to charity
    print("Would you like to take it or donate it to charity?")
    keepthechange = input("Enter 'A' for change and 'B' to donate: ").upper()
    
    while True:
        # if the user would like to receive, then this will be followed
        if keepthechange == "A":
            print("\nDispensing change.\n")
            print("Come again soon. Thank you!\n")
            break
        
        # if the user decides to donate for charity,
        # the user will be informed and the money will be stored for charity
        elif keepthechange == "B":
            print("\nAlright! The rest of your change will be donated to charity.\n")
            print("Come again soon. Thank You!\n")
            break
        
        else:
            # if the input is not "A" nor "B," then this will be followed
            print("\nInvalid input. Please try again.\n")
            break



# finally finished ahhhhh!!!!!  
