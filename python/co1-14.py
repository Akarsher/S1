#14.	Accept an integer n and compute n+nn+nnn.
x=int(input("Enter an Integer : "))
n1 = int(f"{x}") # nn 
n2 = int(f"{x}{x}") # nn
n3 = int(f"{x}{x}{x}") #nnn
print(n1,"+",n2,"+",n3," = ",n1+n2+n3)