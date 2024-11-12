#3. (a)	Generate positive list of numbers from a given list of integers
l=[int(i) for i in input("Enter list of integers : ").split()]
p=[i for i in l if i>=0]
print("Positive Integers : ",p)