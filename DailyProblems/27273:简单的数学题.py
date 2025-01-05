import math
t=int(input())
a=0
list=[]
while 2**a<=1100000:
    list.append(2**a)
    a+=1
for j in range(t):
    n=int(input())
    sum=int((1+n)*n/2)
    i=0
    while list[i]<=n:
        sum-=list[i]*2
        i+=1
    print(sum)