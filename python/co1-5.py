#5.	Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.

l=[int(i) for i in input("Enter List : ").split()]
new=['Over' if i>100 else i for i in l]
print("New List : ",new)