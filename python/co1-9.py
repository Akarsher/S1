#9.	Create a string from given string where first and last characters exchanged

s=input("Enter a String : ")
f=s[0]
l=s[-1:]

print("New String : ",l+s[1:-1]+f)