arr = [30,28,15,24,21,22]
largest=float('-inf')
second_largest=float('-inf')
smallest=float('inf')
second_smallest=float('inf')

for num in arr:
    if num < smallest:
        second_smallest=smallest
        smallest=num
    elif smallest<num<second_smallest:
        second_smallest=num
print("Second Smallest:",second_smallest)

for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif largest>num>second_largest:
        second_largest=num
print("Second Largest: ",second_largest)