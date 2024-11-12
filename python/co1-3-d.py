#3.(d)	List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

word=input("Enter a word : ")
ordinal_values = [ord(char) for char in word]
print(f"The ordinal values of the characters in the word '{word}' are: {ordinal_values}")
