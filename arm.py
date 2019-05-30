num=int(input()) 
l1=len(str(num))
sum=0
temp=num
while(temp!=0):
	sum=sum+((temp%10)**l1)
	temp=temp//10
if sum==num:
	print("yes")
else:
	print("no")
