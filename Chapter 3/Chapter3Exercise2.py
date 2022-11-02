# Exercise 2:
# Start with the list you used in Exercise 1, but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same,
# but each message should be personalized with the person’s name.

print("\nExercise 2\n")

# here, i used the same list of strings from the previous exercise
friends = ["iashlayne", "kristian", "rafael", "patricia", "ysabelle", "krunch", "renzie"]

# and here, instead of printing the strings alone...
# i concatenated them with different ways to say "hello" in other languages
print("Hi, " + friends[0].title() + "!")
print("Salut," + friends[1].title() + "!")
print("Ciao, " + friends[2].title() + "!")
print("Hola, " + friends[3].title() + "!")
print("Annyeonghaseo, " + friends[4].title() + "!")
print("Konnichiwa, " + friends[5].title() + "!")