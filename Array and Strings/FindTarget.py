def find_target(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return-1
arr=[2,6,4,9,5]
target=5
if find_target(arr, target) != -1:
    print("Target found at index:", find_target(arr, target))
else:
    print("Target not found")