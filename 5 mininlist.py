print("find the smallest number in the list")
n=int(input("enter limit"))
l1=[]
m=1
while n>=m :
    l1.append(int(input("enter number : ")))
    m=m+1
print("the smallest number in the list is",min(l1))