# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>昂奕 化学与分子工程学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：dfs，但是@lru_cache在第二遍大循环的时候如果传入相同的参数不会再执行函数体导致结果出错

代码：

```python
import sys
sys.setrecursionlimit(1<<30)

def dfs(x,y):
    global S
    d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    mat[x][y]='.'
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
            if mat[nx][ny]=='W':
                S+=1
                dfs(nx,ny)

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    mat=[]
    for i in range(n):
        mat.append(list(input()))
    maxs=0
    for i in range(n):
        for j in range(m):
            if mat[i][j]=='W':
                S=1
                dfs(i,j)
                maxs=max(S,maxs)
    print(maxs)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-11-21 15.33.45.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-11-21%2015.33.45.png)
### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：
模板题
代码：

```python
from collections import deque


def bfs(x,y):
    q=deque([(x,y,0)])
    d=[(-1,0),(0,1),(0,-1),(1,0)]
    while q:
        x,y,cnt=q.popleft()
        if mat[x][y]==1:
            return cnt
        mat[x][y]=2
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
                if mat[nx][ny]==0:
                    q.append((nx,ny,cnt+1))
                elif mat[nx][ny]==1:
                    return cnt+1
    else:return('NO')
n,m=map(int,input().split())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
print(bfs(0,0))
```

代码运行截图 ==（至少包含有"Accepted"）==

### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：
dfs就完了
代码：

```python
#pylint:skip-file
def dfs(x,y,cnt):
    global n,m,path,mat
    d=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
    if cnt==n*m:
        path+=1
        return
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and mat[nx][ny]==0:

            mat[x][y]=1
            dfs(nx,ny,cnt+1)
            mat[x][y]=0
t=int(input())
for i in range(t):
    n,m,x,y=map(int,input().split())
    path=0
    mat=[[0]*m for _ in range(n)]
    dfs(x,y,1)
    print(path)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-11-23 15.45.57.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-11-23%2015.45.57.png)
### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：
dfs.我把当成上一题只能往右往下走WA了三次...
代码：

```python
path=[]
max_path=[]
w=0
wmax=-999999
def dfs(x,y):
    global n,m,w,wmax,max_path
    w+=mat[x][y]
    path.append((x,y))
    d=[(1,0),(0,1),(-1,0),(0,-1)]
    if (x,y)==(n,m):
        #print(f'终点\npath={path},\nw={w}')
        if w>wmax:
            wmax=w
            max_path=path[:]
        path.pop(-1)
        w-=mat[x][y]
        return
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 1<=nx<=n and 1<=ny<=m and not visited[nx][ny]:
            visited[x][y]=1
            dfs(nx,ny)
            visited[x][y]=0
    path.pop(-1)
    w-=mat[x][y]
n,m=map(int,input().split())
mat=[[0]*(1+m)]
for i in range(n):
    mat.append([0]+list(map(int,input().split())))
visited=[[0]*(1+m) for _ in range(n+1)]
dfs(1,1)
for i in max_path:
    print(*i,sep=' ')

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-11-23 16.26.47.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-11-23%2016.26.47.png)
### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：
dp,创建一个和网格同样大小的矩阵，里面存的是相应的每个位置有多少种不同的方法可到。
dp[x][y]=dp[x-1][y]+dp[x][y-1]
代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0][1]=1
        for x in range(1,m+1):
            for y in range(1,n+1):
                dp[x][y]=dp[x-1][y]+dp[x][y-1]
        return(dp[m][n])
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-11-23 16.35.45.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-11-23%2016.35.45.png)
### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：
dfs。
代码：

```python
import math
blessed=False
def dfs(num):
    global blessed
    for i in range(1,len(num)+1):
        rt=math.sqrt(int(num[0:i]))
        if rt%1==0 and rt!=0:
            if i==len(num):
                blessed=True
                return
            else:
                dfs(num[i:])
    else:
        return
n=input()
dfs(n)
if blessed:print('Yes')
else:print('No')
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-11-23 16.47.01.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-11-23%2016.47.01.png)
## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

正在补OJ选做题...dp还是还是不太会