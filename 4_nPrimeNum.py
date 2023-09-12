n = int(input("Enter a number: "))
m =2
while m<=n :
    i=2
    while i<m :
        if m%i ==0 :
           break
        else:
           i=i+1
    if i==m :
        print(i,end=" ")
    m=m+1