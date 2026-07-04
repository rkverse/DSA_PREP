arr = [8, 7, 1, 6, 5, 9]
n = len(arr)
arr2=[]

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

mid = (n + 1) // 2

for i in range(mid):
    arr2.append(arr[i])

for i in range(n - 1, mid - 1, -1):
    arr2.append(arr[i])

print(arr2)