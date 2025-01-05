n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
ans=[]
tmp=[i for i in range(k)]
def comb(arr,k,cur=0):
    #print('cur,tmp',cur,tmp)
    for q in range(tmp[cur],len(arr)):
        tmp[cur]=q
        for i in range(cur+1,len(tmp)):
            tmp[i]=tmp[cur]+i-cur
        if cur!=k-1:
            #print('cur++')
            comb(arr,k,cur+1)

        else:
            if not ans or list(arr[i] for i in tmp) not in ans:
                ans.append(list(arr[i] for i in tmp))
    #print('cur--')
comb(arr,k)
for i in ans:print(*i,sep=' ')