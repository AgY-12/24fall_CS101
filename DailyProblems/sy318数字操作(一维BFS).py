from collections import deque
def bfs(arr,target):#arr是一个deque,每一项为一个元组(n,i)，n记录这个数是几，i记录这是第几层
    visited = set()
    while arr:
        now=arr.popleft()
        if now[0] not in visited:
            visited.add(now[0])
            arr+=[(now[0]+1,now[1]+1),(now[0]*2,now[1]+1)]
            if now[0]==target:
                return now[1]
t=int(input())
a=deque([(1,0)])
print(bfs(a,t))
