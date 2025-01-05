import math
def ES(n):
    isprime=[True for _ in range(n+1)]
    prime=[]
    for i in range(2,n+1):
        if isprime[i]:
            prime.append(i)
        for j in range(len(prime)):
            if  i*prime[j]>n:break
            isprime[i*prime[j]]=False
            if i%prime[j]==0 :break

    return prime

n=int(input())
a=list(map(int,input().split()))
prime=set(ES(int(max(a)**0.5)+1))
for i in a:
    if math.sqrt(i)%1==0:
        if int(math.sqrt(i)) in prime:
            print('YES')
        else:print('NO')
    else:print('NO')

#集合救你命