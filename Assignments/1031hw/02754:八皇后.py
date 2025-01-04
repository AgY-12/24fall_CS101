queens=[[0]]
def queen(N):
    for n in range(1,N+1):
        if n==1:
            ans=[[1],[2],[3],[4],[5],[6],[7],[8]]
        else:
            ans=[]
            tmp=queens[n-1]
            for i in range(len(tmp)):
                for j in range(1,9):
                    if j not in tmp[i] :
                        for k in range(len(tmp[i])):
                            if abs(j-tmp[i][k])==n-k-1:
                                break
                        else:
                            ans.append(tmp[i]+[j])
        queens.append(ans)
    return queens
t=int(input())
for i in range(t):
    n=int(input())
    print(*queen(8)[-1][n-1],sep='')
'''
[1,5,8,6,3,7,2,4]
'''

