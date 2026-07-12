num=int(input("Enter number: "))
arr=[]
for i in range(2,num-1):
    if num%i==0:
        for j in range(2,i-1):
            if i%j!=0:
                arr.append(i)
for k in range(len(arr)):
    print(arr[k])
