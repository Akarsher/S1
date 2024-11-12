#3. (c)	Form a list of vowels selected from a given word

word=input("Enter word : ")
vowels = "aeiouAEIOU"
vowel_list = [i for i in word if i in vowels]
print("Vowels in ",word," : ",vowel_list)
