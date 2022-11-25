# Program 9

print("\nWelcome to String Occurence Checker!\n")

count = 0

string = input("Enter a string: ").lower()
char = input("Enter a letter you want me to look for: ").lower()

for a in string:
    if a in string:
        if a == char:
            count += 1
print(f"\nThe number of times {char} appeared in your word is {count}.")

print("\nThank you for using my program!\n")