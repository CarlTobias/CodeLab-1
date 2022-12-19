# arrays!

listed = ["alpha", "bravo", "charlie", " delta"]

# first, we access index value placed within square brackets

print(list[2])

# second, we add an element at the end of the list

listed.append("echo")
print(list[4])

# third, we insert an element anywhere in the list

listed.insert(1, "foxtrot")
print(list)

# fourth, we remove elements anywhere in the list

listed.pop(1)
print(list)

# fifth, we remove elements at the end of the list

listed.pop()
print(list)

# sixth, we remove elements anywhere in the list in a slightly different way

listed.remove("charlie")
print(list)

# seventh, we remove elements from anywhere in the list in an even more slightly different way

del listed[2]
print(listed)

# eighth, we delete the whole list in its entirety

listed.clear()
print(listed)

# now let's make a new list

listtwo = ["Sims 4", "Valorant", "Apex Legends", "Portal 2", "Stardew Valley"]


# ninth, we sort the list in an alphabetical order PERMANENTLY

listtwo.sort()
print(listtwo)

# since it's permanent, I redefined the list once more for the next step
listtwo = ["Sims 4", "Valorant", "Apex Legends", "Portal 2", "Stardew Valley"]

# tenth, we sort the list in alphabetical order TEMPORARILY

sorted(listtwo)
print(listtwo)

# eleventh, we reverse the elements of the list

listtwo.reverse()
print(listtwo)

# twelfth, we find the length of the list

print(len(listtwo))


# next off, we are going to write a program 

import numpy as np

# we're creating a 0 dimentional array

arr = np.array(50)
print("Zero Dimentional Array: ", arr)

# here, a 1 dimentional array

arr1 = np.array([10, 20, 30, 40 ,50])
print("One Dimentional Array: ", arr1)

# here, a 2 dimentional array
arr2 = np.array([[2, 4, 16], [3, 9, 81]])
print("Two Dimentional Array: ", arr2)

# and finally, a 3 dimentional array
arr3 = np.array([[[1, 1, 1, 1], [2, 2, 2, 2]], [[3, 3, 3, 3], [4, 4, 4, 4]]])
print("Two Dimentional Array: ", arr3)