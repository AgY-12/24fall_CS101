import math
f=[]
def factor(n):
    for i in range (2,int(math.sqrt(n))+2):
        while n%i==0:
            n/=i
            f.append(i)
    if n!=1:f.append(n)
    return f
n=int(input())
factor(n)
#print(f)
mu=1
for i in f:
    if f.count(i)>1:
        mu=0
        break
if mu==0:print(0)
elif len(f)%2==0:print(1)
elif len(f)%2==1:print(-1)