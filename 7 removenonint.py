print("remove all non int values from the list")
n=int(input("enter limit : "))
l1=[]
m=1
while n>=m :
    l1.append(int(input("please enter :")))
    m=m+1
print(l1)
for e in range(-1,l1,-1) :
    if e<0 :
        l1.remove(e)
print(l1)