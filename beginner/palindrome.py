n=raw_input("Enter the number:")
c=n
w=0
while(n>0):
 a=n%10
 w=w*10+a
 n=n/10
 if(n==c):
 print("YES")
 else:
 print("NO")
