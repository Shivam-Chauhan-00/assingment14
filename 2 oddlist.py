print("a list of first N odd natural number")
n=int(input("enter limit :"))
l1=[]
m=1
while n>=m :
    l1.append(2*m-1)
    m=m+1

for e in l1 :
    print(e,end=" ")
    