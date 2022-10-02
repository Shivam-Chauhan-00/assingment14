print("a list of first N natural numbers")
l1=[]
n=int(input("enter the limit :"))
m=1
while n>=m :
    l1.append(m)
    m=m+1
for e in l1 :
    print(e,end=" ")
