n = int(input("Enter number: "))
a=0
b=1
if n==1:
    print(a,end=" ")
if n>=2 :
    print(a,end=" ")
    print(b,end=" ")
for i in range(n-2):
    m = b
    b = a+b
    a = m
    print(b,end=" ")