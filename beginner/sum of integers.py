N=int(input("enter the number1"))
K=int(input("enter the number2"))
d=[]
sum=0
for i in range(0,N):
  e=int(input("enter the list of element "))
  d.append(e)
for j in range(0,K):
  sum=sum+d[j]
print(sum)
