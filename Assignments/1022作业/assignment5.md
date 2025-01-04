# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>昂奕，化学与分子工程学院</mark>

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。

## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：三个周期的高峰日分别建立集合，取交集，找符合条件的最小。

代码：

```python
t=0
while True:
    t+=1
    p,e,i,d=map(int,input().split())
    if p==e==i==d==-1:break
    else:
        a=set(p+k for k in range(0,21252+d-p+1,23))
        b=set(e+k for k in range(0,21252+d-e+1,28))
        c = set(i + k for k in range(0, 21252+d - i + 1, 33))
        Ans=a&b&c
        ans=33333
        for i in Ans:
            if i >d and i<ans:
                ans=i
        print(f'Case {t}: the next triple peak occurs in {ans-d} days.')
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-10-22 21.09.51.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-22%2021.09.51.png)

### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：'''
1：经费不够做武器：
1-1武器数一样多：ans=0
1-2武器更多：如果卖了一件最贵的够做，就卖(但是你只剩一件武器就不能卖了）；否则ans不动了
2：经费够做武器：
2-1 武器一样多：做
2-2 武器更多：做！没必要卖（因为现在卖跟钱不够了再卖没区别）
'''

代码：

```python

p=int(input())
weapons=list(map(int,input().split()))
weapons.sort()
ans=0
while len(weapons)>1:
    #print('p:',p,'weapons:',weapons)
    if p<weapons[0]:
        if ans==0:
            print(ans)
            break
        else:
            if p+weapons[-1]>=weapons[0] and len(weapons)>1:
                p+=weapons.pop()
                ans-=1
    if p>=weapons[0]:
        p-=weapons[0]
        weapons=weapons[1:]
        ans+=1
else:print(ans)
```

代码运行截图 ==（至少包含有"Accepted"）==
![截屏2024-10-22 21.10.15.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-22%2021.10.15.png)

### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：排序。

代码：

```python
n=int(input())
stu=list(map(int,input().split()))
for i in range(n):
    stu[i]=[stu[i],i+1]
stu.sort(key=lambda x:x[0])
print(*(list(stu[i][1] for i in range(n))),sep=' ')
sum=0
for i in range(1,n+1):
    sum+=stu[i-1][0]*(n-i)
print("{:.2f}".format(sum/n))

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-10-23 17.02.23.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-23%2017.02.23.png)

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：模拟。

代码：

```python
import math
haab={'pop':1, 'no':2, 'zip':3, 'zotz':4, 'tzec':5, 'xul':6, 'yoxkin':7,
      'mol':8, 'chen':9, 'yax':10, 'zac':11, 'ceh':12, 'mac':13, 'kankin':14,
      'muan':15, 'pax':16, 'koyab':17, 'cumhu':18,'uayet':19}
tzolkin={1:'imix', 2:'ik', 3 :'akbal', 4 :'kan', 5 :'chicchan',6:'cimi',7:'manik',
 8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',13:'ben',14:'ix',15:'mem',16:'cib'
 ,17:'caban',18:'eznab',19:'canac',0:'ahau'
 }
print(n:=int(input()))
for i in range(n):
    nodh,mh,yh=input().split()
    nodh=int(nodh[0:-1:])
    yh=int(yh)
    d=yh*365+(haab[mh]-1)*20+nodh+1
    yt=math.ceil(d/260)-1
    d%=260
    mt=d%20
    dt=d%13
    if dt==0:dt=13
    print(f'{dt} {tzolkin[mt]} {yt}')


```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-10-22 21.11.20.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-22%2021.11.20.png)

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：最大不重叠区间问题，再加上一个条件：砍的树倒下的范围不能与未被砍倒的树重叠。这里只需要找到这棵树相邻的树（用一个逆映射实现）然后判断这棵相邻树不在放倒范围内。

但是！！！Susie 为什么不让伐木工把树朝着路外面放倒！！！（哭）还有，为什么有的孩子听故事都能听出个题...非要让我想三天T^T

代码：

```python
'''
WHY CAN'T THE WOODCUTTER FELL THE TREES TOWARDS BEYOND THE ROAD?!!
'''
n=int(input())
tree=[]
qujian=[]
biaoji= []
reversemark={}
for i in range(n):
    x,h=map(int,input().split())
    biaoji.append(x)
    reversemark[x]=i
    tree.append((x-h,x,x,-1))
    tree.append((x,x+h,x,1))
tree.sort(key=lambda x: x[1])
end=0
cut=0
#print(tree)
#print(biaoji)
#print(reversemark)
for i in range(len(tree)):
    adjacentree=biaoji[min(reversemark[tree[i][2]]+tree[i][3],len(biaoji)-1)]
    if tree[i][3]==1:
        no_tree_hindering=adjacentree>tree[i][1] or adjacentree==tree[i][2]
    elif tree[i][3]==-1:
        no_tree_hindering=adjacentree<tree[i][0]
    #print(end,no_tree_hindering)
    if end==0 or (tree[i][0]>end and no_tree_hindering):
        #print(end,tree[i])
        end=tree[i][1]
        cut+=1
print(cut)

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：是《算法设计与在线实践》的例题...一个很基础的贪心问题，基本等同于进程检测。之前看了例题，然后自己做了一遍。

代码：

```python
import math
t=0
while True:
    try :
        n,d=map(int,input().split())
        t+=1
    except ValueError:continue
    if n==0 and d==0:break
    else:
        error=0
        islands=[]
        lines=[]
        for _ in range(n):
            x,y=map(int,input().split())
            islands.append((x,y))
            if abs(y)>d:
                error=1
                continue
            lines.append(((x-math.sqrt(d**2-y**2)),(x+math.sqrt(d**2-y**2))))
        lines.sort(key=lambda x:x[1])
        '''
        nong yige dangqian d start he end point
        '''
        if error==1:
            print(f'Case {t}: -1')
        else:
            i=0
            count=1
            while i < n-1:
                end=lines[i][1]
                while i<n-1 and lines[i][0]<=end :
                    i+=1
                if lines[i][0]>end:
                    end=lines[i][1]
                    count+=1
            print(f'Case {t}: {count}')

```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![截屏2024-10-22 21.14.02.png](../../../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-22%2021.14.02.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。OJ开始上难度了...一道题得想一下午甚至两三天。

会写动态规划了，把很久以前没过的拦截导弹过掉了，很开心。

过了选课（话说为什么会有10^5位的验证码...）和排列。

寻找最近的两数之和思路不难，时间不够看了一眼题解就没做了。

</mark>
