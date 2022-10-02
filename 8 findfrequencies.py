print("to print distinct elementws along with thier frequencies of occurrence in the list")
n=int(input("enter limit: "))
l1=[]
m=1
while n>=m :
    l1.append(int(input("enter numbers : ")))
    m=m+1
print(l1)
for e in l1 :
    print(e,"  ",l1.count(e))