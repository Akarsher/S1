#4.	Count the occurrences of each word in a line of text

l=input("Enter a line : ")

words = l.split()
res = {}

for word in words:
    word = word.lower() 
    if word in res:
        res[word] += 1
    else:
        res[word] = 1

for word, count in res.items():
    print(f"'{word}': {count}")
