import heapq
MAXN=float('inf')

def dij(s,mat,e):#注意,s,e分别是起点和终点.点表示为(w,x,y),w=weight[x][y]

    weight=[[MAXN]*len(mat[0]) for _ in range(len(mat))]
    q=[s]
    weight[s[1]][s[2]]=0
    d=[(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        w,x,y=heapq.heappop(q)
        if (x,y)==e:
            return weight[x][y]
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(mat) and 0<=ny<len(mat[0]) and mat[nx][ny]!='#':
                new_w=weight[x][y]+abs(int(mat[nx][ny])-int(mat[x][y]))
                if new_w<weight[nx][ny]:
                    weight[nx][ny]=new_w
                    heapq.heappush(q,(new_w,nx,ny))

    return ('NO')

m,n,p=map(int,input().split())
mat=[]
for i in range(m):
    mat.append(list(input().split()))
for i in range(p):
    x1,y1,x2,y2=map(int,input().split())
    s,e=(0,x1,y1),(x2,y2)
    if mat[x1][y1]!='#' and mat[x2][y2]!='#':
        print(dij(s,mat,e))
    else:print('NO')