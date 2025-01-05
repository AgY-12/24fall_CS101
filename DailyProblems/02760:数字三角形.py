n=int(input())
delta=[]
storage=[[0]*(_+1) for _ in range(n+2)]
for i in range(n):
    delta.append([0]+list(map(int,input().split()))+[0])

    for j in range(i+1):
        storage[i+2][j+1]=max(storage[i+1][j+1],storage[i+1][j])+delta[i][j+1]

print(max(storage[-1]))

