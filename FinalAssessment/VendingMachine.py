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

# this dictionary is only for the snacks
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
          f"Lay's Lover - {bold}CH1{normal}" : ["All Lay's Flavours (Excluding Forno) & Any Drink of Your Choice", "AED 7.50 + Drink"], f"Pringles Heaven - {bold}CH2{normal}" : ["All Pringle Flavours & Any Drink of Your Choice", "AED 9.00 + Drink"],
          f"Snack Pack 1 - {bold}AI1{normal}" : ["Forno (Authentic Cheese), Stix (Slightly Salted), & Water (Mai Dubai)", "AED 8.00"], f"Snack Pack 2 - {bold}AI2{normal}" : ["Lay's (Original), Pringles (Original), & Water (Mai Dubai)", "AED 8.50"],
          f"Brain Freeze 1 - {bold}BF1{normal}" : ["Baskin Robbins (Chocolate) & Oreos", "AED 8.40"], f"Brain Freeze 2 - {bold}BF2{normal}" : ["Baskin Robbins (Vanilla) & Cinnamon Toast Crunch", "AED 11.40"]}

combosprice = {"BC1" : 7.50, "BC2" : 9.00,
               "CH1" : 7.50, "CH2" : 9.00,
               "AI1" : 8.00, "AI2" : 8.50,
               "BF1" : 8.40, "BF2" : 11.40}


# here i define my own functions in order to keep my code short and concise

# this one is for printing the menu
def menu():
    print("Snacks:")
    for AnBnC, one2four1 in food.items():
        print(str(AnBnC) + " - " + str(one2four1))

    print("\n")
    print("Drinks:")
    for DnEnF, one2four2 in drinks.items():
        print(str(DnEnF) + " - " + str(one2four2))

    print("\n")
    print("Extras:")
    for GnHnI, one2four3 in extras.items():
        print(str(GnHnI) + " - " + str(one2four3))

# i made this function so that i dont have to keep repeating input        
def enterAorB():
    input("Enter 'A' for Yes or 'B' for No: ").upper()

# this function is made to ask the user if their input is correct
# i found myself having to repeat this code a lot, so i made a function to make the code length shorter    
def isthatright():
    while True:
                    print("Is that right?")
                    right = enterAorB()
                
                    if right == "Y":
                        print("\nOkay. Moving on.\n")
                        totalprice += add
                        break
                    
                    elif not right == "Y":
                        print("Invalid input. Try Again.\n")
                    
                    else:
                        menu()
                        
                        print("\nWhat would you like to add?")
                        print("If none, enter 'B'\n")
                        add = input("Enter a code: ").upper()
                        
                        if add in menumenu:
                            print(f"You chose {menumenu[add][0]}\n")
                            
                            print("Is that right?")
                            right = enterAorB()
                            if right == "Y":
                                totalprice += add
                                break


# here, i defined a variable for the final price
totalprice = 0

# here is a welcoming line
print(f"\n{bold}Welcome to Vendimus Prime!{normal}\n\n")

# and the menu is immediately printed
print(f"{bold}Menu:{normal}\n")
menu()

# i told the program to ask the user first if they wanted to buy a combo for a faster purchase
print("\n\nDo you want to purchase one of our combos for a quick purchase?")
# here i put input for their choice
quickies = input(f"Enter '{bold}A{normal}' for Yes or '{bold}B{normal}' for No: ").upper()

# this if-else statement makes the choice on which block of code to run

if quickies == "A":
    # if the user inputs "A," then the program will print the list of the combos
    print("Combos:\n")
    for com, bos in combos.items():
        print(str(com) + " - " + str(bos))
    
    # and after that, i made a while statement that asks for another input for the ccombo code
    run = True
    while run:
        print("\n\nWhat combo would you like to purchase?")
        print(f"If none, enter '{bold}B{normal}'\n")
        comboinput = input("Please enter the corresponding code for the combo: ").upper()
        # when you press b... it goes straight to the end, so fix it to where it will be going to the individual purchase process

        # inside the while loop, there is another if-else statement
        if comboinput == "B":
            # if the user inputs "B," the program will end break the while loop and continue the program
            print("Okay.\n")
            break #idk what to put yet (maybe just say okay and end the prog or go straight to the individual purchases)
        
        elif comboinput in combosprice:
            # otherwise, it will ask the user again just to make sure that they are satisfied with their input
            run2 = True
            while run:
                print(f"You chose {comboinput}.\n")
                print("Is that right?")
                # i used the defined function i made earlier
                right = enterAorB()
                
                if right == "A":
                    # if the input is "A," program will follow the following:
                    print("\nGreat!\n")
                    totalprice += combosprice[comboinput]
                    
                # if the input is neither "A" nor "B," the program will print "Invalid input" and it will repeat the loop 
                elif not right == "A" or not right == "B":
                    print("Invalid input. Try Again.\n")
                
                # otherwise, the program will print the combo menu once again, and the loop will continue
                else:
                    print("Combos:\n")
                    for com, bos in combos.items():
                        print(str(com) + " - " + str(bos))
            run2 = False
        
        # if the input is anything else other than "B" or anything in the combo list,
        # the program will print "Invalid input" and it will repeat the loop
        else:
            print("Invalid input. Please try again.\n")
        run = False
    
        # CONTINUE COMMENTING LATER HEKHEK  
        print("Would you like to add something else?")
        anyother = enterAorB()
        
        if anyother == "A":
            menu()
                
            print("What would you like to add?")
            add = input("Please enter a code: ")
            
            run = True    
            while run:
                if add in menumenu:
                    print(f"You chose {menumenu[add][0]}\n")
                    isthatright()
                        
                break
            
        print("Anything else?")
        anyotherother = enterAorB()
            
        if anyotherother == "Y":
            menu()
                
            print("What would you like to add?")
            add = input("Please enter a code: ")
                
            while True:
                if add in menumenu:
                    print(f"You chose {menumenu[add][0]}\n")
                    isthatright()
                        
                break        
            

elif quickies == "B":
    print("Snacks:")
    for AnBnC, one2four1 in food.items():
        print(str(AnBnC) + " - " + str(one2four1))
        
    run = True
    while run:
        print("\n\nWhat would you like to purchase for snacks?")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose1 = input("Enter a code: ").upper()
    
        if choose1 == "B":
            print("Okay.\n")
            break #idk what to put yet (maybe just say okay and end the prog or go straight to the individual purchases)
        
        elif choose1 in food:
            run2 = True
            while run2:
                print(f"You chose {bold}{choose1}{normal}.\n")
                print("Is that right?")
                right = enterAorB()
                
                if right == "A":
                    print("\nGreat!\n")
                    totalprice += foodprice[choose1]
                    
                # this is currently infinite... fix this
                elif not right == "A" or not right == "B":
                    print("Invalid input. Try Again.\n")
                
                else:
                    print("Snacks:")
                    for AnBnC, one2four1 in food.items():
                        print(str(AnBnC) + " - " + str(one2four1))
            run2 = False
        
        else:
            print("Invalid input. Please try again.\n")
        run = False
    
    
    
    print("Drinks:")
    for DnEnF, one2four2 in drinks.items():
        print(str(DnEnF) + " - " + str(one2four2))
        
    run3 = True
    while run3:
        print("\n\nWhat would you like to purchase for drinks?")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose2 = input("Enter a code: ").upper()
    
        if choose2 == "B":
            print("Okay.\n")
            break #idk what to put yet (maybe just say okay and end the prog or go straight to the individual purchases)
        
        elif choose2 in food:
            run4 = True
            while run4:
                print(f"You chose {bold}{choose1}{normal}.\n")
                print("Is that right?")
                right = enterAorB()
                
                if right == "A":
                    print("\nGreat!\n")
                    totalprice += foodprice[choose1]
                    
                # this is currently infinite... fix this
                elif not right == "A" or not right == "B":
                    print("Invalid input. Try Again.\n")
                
                else:
                    print("Drinks:")
                    for DnEnF, one2four2 in drinks.items():
                        print(str(DnEnF) + " - " + str(one2four2))
            run4 = False
        
        else:
            print("Invalid input. Please try again.\n")
        run3 = False
    
    
    
    print("Extras:")
    for GnHnI, one2four3 in extras.items():
        print(str(GnHnI) + " - " + str(one2four3))
        
    run5 = True
    while run5:
        print("\n\nWhat would you like to purchase any extras?")
        print(f"If none, enter '{bold}B{normal}'\n")
        choose2 = input("Enter a code: ").upper()
    
        if choose2 == "B":
            print("Okay.\n")
            break #idk what to put yet (maybe just say okay and end the prog or go straight to the individual purchases)
        
        elif choose2 in food:
            run6 = True
            while run6:
                print(f"You chose {bold}{choose1}{normal}.\n")
                print("Is that right?")
                right = enterAorB()
                
                if right == "A":
                    print("\nGreat!\n")
                    totalprice += foodprice[choose1]
                    
                # this is currently infinite... fix this
                elif not right == "A" or not right == "B":
                    print("Invalid input. Try Again.\n")
                
                print("Extras:")
                for GnHnI, one2four3 in extras.items():
                    print(str(GnHnI) + " - " + str(one2four3))
            run6 = False
        
        else:
            print("Invalid input. Please try again.\n")
        run5 = False




print("Thank you for using Vendimus Prime!\n")
    
print(f"Your total is {totalprice}.")
print("\nTo purchase, please insert money.\n")

# these three lines inform the user of the useable bills and coins,
# and it also informs the user that the minimum amount to be able to purchase anything is 3 dhs
print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
print("All coins are accepted.\n")
print(f"The minimum amount is {bold}AED 3{normal}")
        
money = (float(input("\nPlease insert here: ")))
totalmoney =+ money

while money < totalprice:
    print(f"Almost there! Just AED {totalprice - money} left.")
    money = (float(input("\nPlease insert here: ")))
    totalmoney =+ money
    
while True:
    # this is the code the program follows when the criteria is met
        if money >= 3:
            print(f"\nGreat! You inserted a total of {totalmoney} correct?")
            correct = enterAorB()
            
            if correct == "Y":
                break
            
            else:
                print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
                print("All coins are accepted.\n")
                print(f"The minimum amount is {bold}AED 3{normal}")

                money = (float(input("\nPlease insert here: ")))
                totalmoney =+ money

                while money < totalprice:
                    print(f"Almost there! Just AED {totalprice - money} left.")
                    money = (float(input("\nPlease insert here: ")))
                    totalmoney =+ money
            break
        
        # and this is what is followed when the money inserted is invalid    
        else:
            # and i had the program ask the user again for money input
            print(f"\n{bold}Invalid bill/s or coin/s.{normal}")
            print("Please try again.\n")
            
            print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
            print("All coins are accepted.\n")
            print(f"The minimum amount is {bold}AED 3{normal}")
            
            money = (float(input("\nPlease insert here: ")))
            totalmoney =+ money
            
            while money < totalprice:
                print(f"Almost there! Just AED {totalprice - money} left.")
                money = (float(input("\nPlease insert here: ")))
                totalmoney =+ money

change = totalprice - totalmoney

if change <= 0:
    print("You have no change.\n")
    print("Come again soon. Thank you!\n")

elif change <= 0.24 or change > 0.49 <= 0.26 or change > 0.74 <= 0.51 or change > 0.99 <= 0.76:
    print("You have no change.\n")
    print("Come again soon. Thank you!\n")

else:
    print(f"Your change is AED {change}\n")
    
    print("Would you like to take it or donate it to charity?")
    keepthechange = input("Enter 'A' for change and 'B' to donate: ").upper()
    
    while True:
        if keepthechange == "A":
            print("Dispensing change.\n")
            print("Come again soon. Thank you!\n")
            break
        
        elif not keepthechange == "Y" or not keepthechange == "N":
            print("Invalid input. Please try again.")
        
        else:
            print("Alright! The rest of your change will be donated to charity.\n")
            print("Come again soon. Thank You!\n")
            break
    
    
    
    

    
print("\nTo purchase, please insert credit.\n")

# these three lines inform the user of the useable bills and coins,
# and it also informs the user that the minimum amount to be able to purchase anything is 3 dhs
print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
print("All coins are accepted.\n")
print(f"The minimum amount is {bold}AED 3{normal}")

# here i put an input function where the user will give money
money = (float(input("\nPlease insert here: ")))
# and here, i made it so that the money inputted will be added to the credit variable
credit =+ money

# here i added a (sort of) infinite while loop that asks the user over and over again until a specific amount (3 dhs) is met
while True:
    # this is the code the program follows when the criteria is met
    if money >= 3:
        print(f"\nGreat! Your current balance is now: {credit}\n")
        break
    
    # this is what is followed if credit is too low
    elif money < 3 >= 0.25:
        print(f"\n{bold}Amount too low to purchase.{normal}")
        print("Please insert more credit.\n")
        
        print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
        print("All coins are accepted.\n")
        print(f"The minimum amount is {bold}AED 3{normal}")

        money2 = (float(input("\nPlease insert credit here: ")))
        # and the money inputted here will be added to the original money variable
        # to be totalled for the credit
        money =+ money2
        # the same thing happens here
        credit = money
    
    # and this is what is followed when the money inserted is invalid    
    else:
        # and i had the program ask the user again for money input
        print(f"\n{bold}Invalid bill/s or coin/s.{normal}")
        print("Please try again.\n")
        
        print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
        print("All coins are accepted.\n")
        print(f"The minimum amount is {bold}AED 3{normal}")

        money2 = (float(input("\nPlease insert here: ")))
        # the same thing is done here


# if purchase is over 20 dhs give a free item from the machine

# im so tired loll