#7.	Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to same value (c) whether any value occur in both

l1=[int(i) for i in input("Enter List 1 : ").split()]
l2=[int(i) for i in input("Enter List 2 : ").split()]

#a
if len(l1) == len(l2):
    print("Length is same.")
else:
    print("Length is not same!")

#b
if sum(l1) == sum(l2) :
    print("Sum of Lists are equal.")
else:
    print("Sum is not equal!")

#c
c=set(l1).intersection(set(l2))
if len(c) != 0:
    print("Values : ",c)
else:
    print("No common elements!")