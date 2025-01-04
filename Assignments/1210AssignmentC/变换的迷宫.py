import heapq
MAXN=float('inf')

def dead(x0,y0):
    return mat[x0-1][y0]==mat[x0][y0-1]==mat[x0+1][y0]==mat[x0][y0+1]=='#' and mat[x0][y0]=='.' and k>2

def dij(s,mat):
    global k
    weight=[[MAXN]*len(mat[0]) for __ in range(len(mat))]
    q=[s]
    weight[s[1]][s[2]]=0
    d=[(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        w,x,y=heapq.heappop(q)
        #print((w,x,y))
        if mat[x][y]=='E':
            return w
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 1<=nx<len(mat)-1 and 1<=ny<len(mat[0])-1 :
                if mat[nx][ny] in {'.','E','S'} and weight[nx][ny]>w+1 and not dead(nx,ny):
                    weight[nx][ny]=w+1
                    heapq.heappush(q,(w+1,nx,ny))
                elif mat[nx][ny]=='#' and not(w%2==0 and k%2==0) and mat[x][y]!='#':

                    tmp=w+1#找到到这个#的最短路径长
                    while tmp%k!=0:
                        tmp+=2

                    if weight[nx][ny]>tmp:#更新最短路径,入队
                        weight[nx][ny]=tmp
                        heapq.heappush(q,(tmp,nx,ny))
    return 'Oop!'

t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    mat=['#'*(m+2)]
    s,x0,y0=(),0,0
    for i in range(n):
        mat.append(['#']+list(input())+['#'])
        if 'S' in mat[i]:
            x0,y0=i,mat[i].index('S')
            s=(0,x0,y0)
    mat.append(['#']*(m+2))
    #for _ in mat:
    #    print(*_)
    if mat[x0-1][y0]==mat[x0][y0-1]==mat[x0+1][y0]==mat[x0][y0+1]=='#':
        print('Oop!')
    else:
        print(dij(s,mat))