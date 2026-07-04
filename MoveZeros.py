arr=[15,30,0,21,0,3]
left=0
for right in range(len(arr)):
    if arr[right]==0:  # arr[right] != 0 ( if 0 should be at end of array )
        arr[right],arr[left]=arr[left],arr[right]
        left+=1
print(arr)