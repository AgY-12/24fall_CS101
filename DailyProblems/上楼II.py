def sl(n):
    for i in range(1,3):
        n-=i
        sl(n)

n=int(input())
print(sl(n)%10007)