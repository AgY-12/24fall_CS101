d=int(input())
n=int(input())
mat=[[0]*1025 for _ in range(1025)]
maxs=[0]
for _ in range(n):
    x,y,z=map(int,input().split())
    for i in range(max(x-d,0),min(x+d,1024)+1):
        for j in range(max(y-d,0),min(y+d,1024)+1):
            mat[i][j]+=z
            if mat[i][j]>=maxs[-1]:
                maxs.append(mat[i][j])
ans1=0
ans2=maxs[-1]
while True:
    ans1+=1
    if len(maxs)==1 or maxs.pop()!=maxs[-1]:break
print(ans1,ans2)
