#pylint:skip-file
#TLE,呜呜呜呜
import sys

def dfs(x,y,s,dr):
    global w,h,mat,gans
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    #print('x,y.s.dr:',x,y,s,dr)
    if s>gans:return
    for id in range(len(d)):
        nx,ny=x+d[id][0],y+d[id][1]
        if 0<=nx<=w+1 and 0<=ny<=h+1:
            #print('ny,nx:',ny,nx)
            if (nx,ny)==(x2,y2):
                gans=min(gans,s+1)
            if mat[ny][nx]==' ':
                #print('s:',s)
                if s==0:
                    #print(f'dfs({nx},{ny},{s+1},{id})')
                    segmnet=dfs(nx,ny,s+1,id)
                if mat[y][x]==' ':
                    mat[y][x]='X'
                    #print(f'往下走:s={s}')
                    if dr!=id:
                        dfs(nx,ny,s+1,id)
                    else:
                        dfs(nx,ny,s,id)
                    #print(f'回到{x},{y},{s},{id}')
                    mat[y][x]=' '
                    #print('segment:',segment)
                    #print(ans)
    #print(ans)
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
        mat.append([' ']+list(input[id])+[' '])
        id+=1
    mat.append([' '] * (w + 2))
    #print('mat:',mat)
    pair=0
    print(f'Board #{board}:')
    while True:
        gans = 99999
        pair+=1
        x1,y1,x2,y2=map(int,input[id].rstrip('\n').split())
        id+=1
        if (x1,y1,x2,y2)==(0,0,0,0):break
        dfs(x1,y1,0,0)
        if gans!=99999:
            print(f'Pair {pair}: {gans} segments.')
        else:print(f'Pair {pair}: impossible.')