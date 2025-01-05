def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if hi==None:hi=len(a)
    if key is None:
         while lo < hi:
             mid = (lo + hi) // 2
             if a[mid] > x:
                 lo = mid + 1
             else:
                hi = mid
    else:
         while lo < hi:
             mid = (lo + hi) // 2
             if key(a[mid]) > key(x):
                 lo = mid + 1
             else:
                hi = mid
    return lo
def bisect_right(a, x, lo=0, hi=None, *, key=None):
    if hi==None:hi=len(a)
    if key is None:
         while lo < hi:
             mid = (lo + hi) // 2
             if a[mid] >= x:
                 lo = mid + 1
             else:
                hi = mid
    else:
         while lo < hi:
             mid = (lo + hi) // 2
             if key(a[mid]) >= key(x):
                 lo = mid + 1
             else:
                hi = mid
    return lo
t=int(input())

for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    a=[]
    for i in range(0,len(b),2):
        a.append((b[i],b[i+1]))
    buckets=[[] for _ in range(5007)]
    for i in range(len(a)):
        cur=0
        while buckets[cur]:
            print('buckets',buckets[0:5])
            print('ai',a[i])
            find=bisect_left(buckets[cur],a[i],key=lambda x:x[0])
            hi=bisect_right(buckets[cur],a[i],key=lambda x:x[0])
            print('find0',find)
            find=bisect_left(buckets[cur],a[i],lo=find,hi=hi,key=lambda x:x[1])
            print('find1',find)
            print('stick:',a[i])
            print('buckets[cur]',buckets[cur])
            if  len(buckets[cur])>find>0 and buckets[cur][find-1][1]<a[i][1]:
                cur += 1
                continue
            elif (find==0 and buckets[cur][find][1]>a[i][1]) or (find==len(buckets[cur]) and buckets[cur][find-1][1]<a[i][1]):
                cur+=1
                continue
            else:
                buckets[cur].insert(find,a[i])
                break
        else:
            buckets[cur].append(a[i])
    ans=buckets.index([])
    print(ans)
    #print(buckets[0:ans])
'''
算法有问题！
5 
4 9 5 2 2 1 3 5 1 4 
过不去
'''