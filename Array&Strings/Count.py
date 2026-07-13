pst=0
ngt=0
zero=0
n=int(input("Enter range: "))
for i in range(n):
    num=int(input("Enter number: "))
    if num>0:
        pst+=1
    elif num<0:
        ngt+=1
    else:
        zero+=1
print("Positive numbers:", pst)
print("Negative numbers:", ngt)
print("Zeroes:", zero)