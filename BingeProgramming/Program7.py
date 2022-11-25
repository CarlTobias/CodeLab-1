# Program 7

palindrome = input("Enter a word: ").upper()

pal = palindrome.upper()

rpalindrome = palindrome[::-1]

if palindrome == rpalindrome:
    print("\nYour word is a palindrome.")

else:
    print("\nYour word is not a palindrome.")

print("Thank you for using my program!\n")