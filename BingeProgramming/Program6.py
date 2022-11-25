# Program 6

print("\nWelcome to the Fibonacci Program!\n")
fibterms = int(input("How many terms would you like me to show? "))

term1, term2 = 0, 1

count = 0

if fibterms <= 0:
    print("\nInvalid number.") 
    print("\nEnter a positive integer: ")

elif fibterms == 1:
    print(f"Fibonacci Sequence of {fibterms}:")
    print(term1)

else:
    print(f"Fibonacci Sequence of {fibterms}:")
    
    while count <= fibterms:
        print(term1)
        nth = term1 + term2

        term1 = term2
        term2 = nth
        count += 1