print("a list of first N even natural numbers")
n=int(input("enter the limit :"))
l1=[]
m=1
while n>=m :
    l1.append(2*m)
    m=m+1
for e in l1 :
    print(e,end=" ")