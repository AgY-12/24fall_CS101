def A(n):
    if len(n) == 1:
        return [n]
    else:
        ans=[]
        for i in range(len(n)):
            tmp=A(n[:i]+n[i+1:])
            for j in tmp:
                ans.append([n[i]]+j)
        return ans
x=int(input())
n=list(range(1,x+1))
for i in A(n):
    print(*i,sep=' ')