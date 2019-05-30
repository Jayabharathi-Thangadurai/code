def prime(num):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count==1:
        return True

n,m=map(int,input().split())
for k in range(n+1,m):
    if prime(k):
        print(k,end=" ")
