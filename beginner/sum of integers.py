n=int(input("enter the number1"))
k=int(input("enter the number2"))
d=[]
sum=0
for i in range(0,n):
  e=int(input("enter the list of element "))
  d.append(e)
for j in range(0,k):
  sum=sum+d[j]
print(sum)
