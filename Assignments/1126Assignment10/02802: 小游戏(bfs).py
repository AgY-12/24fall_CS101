from collections import deque
import sys
from copy import deepcopy
def bfs(x,y):
    matc=deepcopy(mat)
    q=deque([(x,y,0,0)])#分别是x,y,线段数,来时的方向
    d=[(-1,0),(0,1),(0,-1),(1,0)]
    ans=99999
    ss=[[99999]*(w+2) for _ in range(h+2)]
    while q:
        #print(q)
        x,y,s,dr=q.popleft()
        #print(f'正在{x},{y}')
        for cntdr in range(len(d)):
            dx,dy=d[cntdr]
            nx,ny=x+dx,y+dy

            if 0<=nx<=w+1 and 0<=ny<=h+1:
                #print(f'正在探{nx},{ny},该位置是{mat[ny][nx]}')
                #这个ans存的是当前已经到终点的路的最小线段数,如果走到了哪个位置发现s已经>这个ans了,就不用再走这个位置了
                if (nx,ny)==(x2,y2):
                    #print(f'看到终点,当前位置:{x},{y},终点在{cntdr}方,来时方向{dr},s={s}')
                    ans = min(s+1 if cntdr!=dr or s==0 else s,ans)
                    #print('ans:',ans)
                    ss[ny][nx]=ans
                #print(f'matc[{ny}][{nx}]=={matc[ny][nx]}')
                if matc[ny][nx]==' ' or (matc[ny][nx]=='V' and ss[y][x]>=s):
                    if cntdr==dr and s<=ans and s!=0:
                        q.append((nx,ny,s,cntdr))
                    elif s+1<=ans:
                        q.append((nx,ny,s+1,cntdr))
                #print(f'路探过了,q={q}')
        matc[y][x]='V'
        ss[y][x]=min(ss[y][x],s)
    #for _ in ss:
    #    print(*_,sep=' ')
    return ans

input=sys.stdin.readlines()
id=0
board=0
while True:
    board+=1
    w,h=map(int,input[id].split())
    if (w,h)==(0,0):break
    id+=1
    mat=[[' ']*(w+2)]
    for i in range(h):
        mat.append([' ']+list(input[id].rstrip('\n'))+[' '])
        id+=1
    mat.append([' '] * (w + 2))
    #print('mat:',mat)
    pair=0
    print(f'Board #{board}:')
    while True:
        pair+=1
        x1,y1,x2,y2=map(int,input[id].rstrip('\n').split())
        id+=1
        if (x1,y1,x2,y2)==(0,0,0,0):break
        a=bfs(x1,y1)
        if a!=99999:
            print(f'Pair {pair}: {a} segments.')
        else:print(f'Pair {pair}: impossible.')
    print('')
'''
5 5
XXXXX
    X
 XXX
 XX
 X  X
5 1 4 1
0 0 0 0
5 4
XXXXX
X   X
XXX X
 XXX 
2 3 5 3
1 3 4 4
2 3 3 4
0 0 0 0
5 5
XXX X
X X X
    X
X  XX
X XXX
1 2 3 5
1 2 3 2
1 2 1 4
1 2 1 5
0 0 0 0
3 3
X X
 X 
 XX
1 1 3 3
1 1 2 3
2 2 3 3
0 0 0 0
0 0
 '''