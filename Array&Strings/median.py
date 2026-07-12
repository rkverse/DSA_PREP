arr = [8, 7, 1, 6, 5, 9]
n = len(arr)
mid=(len(arr)-1)//2
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
print("Median of the array: ",arr[mid])