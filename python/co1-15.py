#15.	Print out all colors from color-list1 not contained in color-list2.
l1=[i for i in input("Enter List 1 : ").split()]
l2=[i for i in input("Enter List 2 : ").split()]
r=[i for i in l1 if i not in l2]
print("Result : ",r)
