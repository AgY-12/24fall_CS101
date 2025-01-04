n=int(input())
coins=list(map(int,input().split()))
coins.sort(reverse=True)
s=sum(coins)
num=0
money=0
for i in coins:
    num+=1
    money+=i
    if money>s/2:break
print(num)