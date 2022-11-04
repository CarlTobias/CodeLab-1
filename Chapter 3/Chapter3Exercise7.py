# Exercise 7:
# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.

# Print your list in its original order.
# Don’t worry about printing the list neatly, just print it as a raw Python list.

# Use sorted() to print your list in alphabetical order without modifying the actual list.

# Show that your list is still in its original order by printing it.

# Use sorted() to print your list in reverse alphabetical order
# without changing the order of the original list.

# Show that your list is still in its original order by printing it again.

# Use reverse() to change the order of your list.
# Print the list to show that its order has changed.

# Use reverse() to change the order of your list again.
# Print the list to show it’s back to its original order.

# Use sort() to change your list so it’s stored in alphabetical order.
# Print the list to show that its order has been changed.

# Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

print("\nExercise 7\n")

# first, i made a list of all the places that i'd like to visit and printed it with concatenated text
travel = ["United Kingdom", "France", "Italy", "Sweden", "Maldives"]
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

# next, i sorted the list using the "sorted()" function,
# but i moved that to a variable named "sortedtravel" so that i don't actually modify the list
# to prove that, i printed the list with concatenated text
print(sorted(travel))

# here, i did essentially the same thing, but instead of sorting alphabetically,
# i did it in reverse alphabetical order... and again, i did this without reversing the original list
# and to prove that, i printed the list again with concatenated text
print(str(sorted(travel, reverse=True)) + "\n")

# here, i used the "reverse()" function to reverse the actual list
#i then printed the list once more with concatenated text (to prove that the command worked)
travel.reverse()
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

# i repeated lines 56 to 59 to reverse the original list to its original state
travel.reverse()
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

# now that it's back to its original state, i used the "sort()" function to sort it alphabetically
# i also, once again, printed the list with concatenated text (to prove that the command worked)
travel.sort()
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

# and finally, i used the reversed version of the "sort()" function
# to sort it in reverse alphabetical order
# i then printed the list for a final time with concatenated text to prove that the command worked
travel.sort(reverse = True)
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")