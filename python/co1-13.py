#13.	Create a list of colors from comma-separated color names entered by user. Display first and last colors.
c=input("Enter Colors : ")
colors=[i.strip() for i in c.split(",")]
print("First Color : ",colors[0],"\nLast Color : ",colors[-1])