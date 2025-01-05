from collections import Counter

t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    max, min = 0, 9999999
    for j in range(n):
        s, d = map(int, input().split())
        if d > max: max = d
        if s < min: min = s
        
        counter=Counter(a)

    '''
    for j in range(n):
        s,d=map(int,input().split())
        if d>max:max=d
        if s<min:min=s
        a[j]=list(range(s,d+1))
    time=[]
    for j in a.values():
        time.union(j)
    counter=Counter(time)
'''