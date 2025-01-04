import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(b*math.ceil(a/b)-a)
