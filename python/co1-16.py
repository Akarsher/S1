#16.	Create a single string separated with space from two strings by swapping the character at position 1.
s1=input("Enter String 1 :")
s2=input("Enter String 2 :")
new1=s1[0]+s2[1]+s1[2:]
new2=s2[0]+s1[1]+s2[2:]
print("New String : ",new1," ",new2)