num=int(input())
Fact=1
if(num<0):
  print("Invalid")
elif(num==0):
  print(1)
else:
  for i in range(1,num+1):
    Fact=Fact*i
  print(Fact)
