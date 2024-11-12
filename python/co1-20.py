"""from the list of integers create a list removing even numbers"""

oldList=[int(i) for i in input("Enter the numbers").split()]

newList=[i for i in oldList if i%2!=0]

print("List after removing even numbers:",newList)