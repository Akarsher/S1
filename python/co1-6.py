#6.	Store a list of first names. Count the occurrences of ‘a’ within the list
import math

l=[i for i in input("Enter List : ").split()]
count=0
for i in l:
    count+= i.lower().count('a')
print("Count of Letter A : ",count)