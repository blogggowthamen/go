n=input("Enter a number to find factorial: ")
r=1
if n>0:
	for x in range(1,n+1):
		 r=r*x
	print (r)
else:
	print ("Enter a positive number")
