#17. Sort dictionary in ascending and descending order.

d = { 
    'apple': 3, 
    'banana': 1, 
    'cherry': 2, 
    'date': 5, 
    'blueberry': 4 
}

#ascending
print("Ascending Order : ",dict(sorted(d.items())))

#descending
print("Descending Order : ",dict(sorted(d.items(),reverse=True)))

