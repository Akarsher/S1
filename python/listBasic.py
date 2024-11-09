list=["S1MCA","Akhil"]
print(list)
print("Length is:",len(list))

print("Name is:",list[1],"\n")


frutList= ["cherry", "orange", "kiwi", "melon", "mango"]
print("Before append:",frutList,"\n")

frutList.append("orange")
print("After append:",frutList,"\n")

frutList.insert(1,"Apple")
print("Added apple at 1st:",frutList,"\n")

numList=['Ford', 'BMW', 'Volvo','Ford', 'BMW', 'Volvo','Ford', 'BMW', 'Volvo']
numList.sort()
print(numList)
""" newList=[]
for x in numList:
	if x>3 in x:
		newList.append(x) """

print(frutList[2:])

print(frutList[-3:-1])

