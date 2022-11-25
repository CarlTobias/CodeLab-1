# 1st and 2nd activity: nested loops and statements

carbrands = ["TESLA", "MASERATI", "ROLLS ROYCE", "LAMBORGHINI"]

tmodels = ["MODEL S", "MODEL 3", "MODEL X", "MODEL Y"]
mmodels = ["GRANTURISMO", "QUATTROPORTE", "MASERATI GHIBLI III"]
rrmodels = ["GHOST", "WRAITH", "DAWN", "PHANTOM"]
lmodels = ["AVENTADOR", "HURACAN", "URUS", "GALLARDO"]

print("\nWelcome to the CAR(l)s Shop!\n")

while True:
    
    whatcar = input("What car would you want to purchase today? ").upper()

    if whatcar in carbrands:
        if whatcar == "TESLA":
            print("Car models available:\n")
            for x in tmodels:
                print("- ", x, "\n")

            carmodel = input(f"What model of {whatcar.title()} would you like? ")

            carcolor = input("\nGreat! What color would you like it in? ")

            print("\nNoted. Please contact us at this number: 052 575 4775\nor this email: thecar(l)shop@gmail.com to finalize your purchase.")
            break
        
        elif whatcar == "MASERATI":
            print("Car models available:\n")
            for x in mmodels:
                print("- ", x, "\n")

            carmodel = input(f"What model of {whatcar.title()} would you like? ")

            carcolor = input("\nGreat! What color would you like it in? ")

            print("\nNoted. Please contact us at this number: 052 575 4775\nor this email: thecar(l)shop@gmail.com to finalize your purchase.")
            break

        
        elif whatcar == "ROLLS ROYCE":
            print("Car models available:\n")
            for x in rrmodels:
                print("- ", x, "\n")

            carmodel = input(f"What model of {whatcar.title()} would you like? ")

            carcolor = input("\nGreat! What color would you like it in? ")

            print("\nNoted. Please contact us at this number: 052 575 4775\nor this email: thecar(l)shop@gmail.com to finalize your purchase.")
            break
        
        elif whatcar == "LAMBORGHINI":
            print("Car models available:\n")
            for x in lmodels:
                print("- ", x, "\n")

            carmodel = input(f"What model of {whatcar.title()} would you like? ")

            carcolor = input("\nGreat! What color would you like it in? ")

            print("\nNoted. Please contact us at this number: 052 575 4775\nor this email: thecar(l)shop@gmail.com to finalize your purchase.")
            break
    else:
        if whatcar == "BENTLEY" or whatcar == "JAGUAR" or whatcar == "PORSCHE" or whatcar == "BMW" or whatcar == "MERCEDES-BENZ":
            print("That car is currently not available here in the shop. Please try again.")

        else:
            print("That car is not available here in the shop. Please try again.")


# 3rd activity: range()

# this line asks the user input for the range we want
pyramidrange = int(input("\nWhat's the range of the pyramid size? "))

# once that is defined, we start a nested for loop

# the first loop says that for every integer within 0 and the range input,
# it will execute the commands inside
for x in range(pyramidrange):
    # this for loop states that for every integer within 0 and x + 1,
    # it will execute the commands inside
    for y in range(0, x + 1):
        print(y, end = " ")
    print()

print("\n")

for x in range(0, pyramidrange):
    for y in range(0, x + 1):
        print("*", end = " ")
    print()

print("\n")

for i in range(0, 55, 5):
    print(i, end = " ")

print("\n")

for i in range(0, 55, 5):
    print(i, end=" ")

print("\n")

for x in range(0, pyramidrange):
    for y in range(0, x + 1):
        print("*", end=" ")
    print()
for x in range(pyramidrange, 0, -1):
    for y in range(x - 1):
        print("*", end=" ")
    print()

print("\n")

for x in range(pyramidrange, 0, -1):
    for y in range(x + 1):
        print(x, end=" ")
    print()

print("\n")

n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    j = 1
    
    while j <= i:
        print((i*2-1), end = " ")
        j = j + 1
    i = i + 1
print()

n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    j = 1

    while j <= i:
        print((i*2), end=" ")
        j = j + 1
    i = i + 1
print()

print("\n")

n = int(input("Enter the number of rows: "))
m = n

for i in range(0, n):
    for j in range(0, m):
        print(end = " ")
    
    m -= 1

    for j in range(0, i + 1):
        print("*", end = " ")
    print()