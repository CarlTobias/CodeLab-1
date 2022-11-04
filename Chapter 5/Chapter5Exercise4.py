# Exercise 4:
# Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

# Use a loop to print the name of each river included in the dictionary.

# Use a loop to print the name of each country included in the dictionary.

print("\nExercise 4\n")

# i created a dictionary named "river" containing different rivers around the world
river = {
    "Amazon River" : "South America",
    "Mississippi River" : "North America", 
    "Nile River" : "Africa",
    "Danube River" : "Europe",
    "Murray River" : "Australia"
}

# next, i printed the following text (indicating that i will be statements containing keys and values):
print("Statements:\n")
# and started a "for" loop that scans for both keys and values in the dictionary
# i added two variables ("kriver" for keys and "vriver" for values)
for kriver, vriver in river.items():
    # inside the for loop, the program is told to print these until all items have been gone through
    print("The " + kriver + " can be found in " + vriver + ".\n")

# here, i printed the following text (indicating that i will be printing just keys):
print("Dictionary Keys:\n")
# this "for" loop is similar to the first one, but instead of ".items(),"
# i used ".keys()" to only scan for keys
for kriver in river.keys():
    # for every key, it will print a key (in order from how i formatted it)
    print(kriver)
print("\n")

# then, i printed the following text (indicating that i will be printing just values):
print("Dictionary Values:\n")
# this "for" loop is similar to the previous ones, but instead of ".items()," or ".keys()"
# i used ".values()" to only scan for values
for vriver in river.values():
    # for every value, it will print a value (in order from how i formatted it)
    print(vriver)
print("\n")
