#8.	Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.

l=input("Enter a String : ")
f=l[0]

l1=l[1:].replace(f,'$')

print("New String : ",f+l1)