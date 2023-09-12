m = int(input("Enter a number: "))
i=2
while i<m :
    if m%i ==0 :
        print("NOT PRIME NUMBER")
        break
    else:
        i=i+1
if i==m :
    print("PRIME NUMBER")

