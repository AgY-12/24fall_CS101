# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by 昂奕，化学与分子工程学院

**说明：**

1）Oct⽉考： AC5 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。

## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/

思路：
略

时间：20min（因为没有注意到k的范围一直RE）

代码

```python
k=int(input())
s=input()
ans=''
for i in s:
    if i>='A' and i<='Z':
        io=ord(i)-k
        while io<65:
            io+=26
        i=chr(io)
    elif i>='a' and i<='z':
            io = ord(i) - k
            while io < 97:
                io += 26
            i= chr(io)
    ans+=i
print(ans)

```

代码运行截图 ==（至少包含有"Accepted"）==

![img_1.png](assets/img_1.png?t=1728626140239)

### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/

思路：

略

时间：2min

代码

```python
a,b=input().split()
a=int(a[0:2:])
b=int(b[0:2:])
print(a+b)

```

代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-11 13.58.41.png](../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-11%2013.58.41.png)

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/

思路：

模拟

时间：6min

代码

```python
xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
jianyan=['1','0','X','9','8','7','6','5','4','3','2']
n=int(input())
for i in range(n):
    s=input()
    jiao=[]
    for j in range(17):
        jiao.append(int(s[j])*xishu[j])
    if jianyan[sum(jiao)%11] == s[-1]:
        print('YES')
    else:print('NO')

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-11 14.04.13.png](../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-11%2014.04.13.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/

思路：

模拟

时间：

代码

```python
n=int(input())
while n>1:
    t=n
    if n%2==0:
        n//=2
        print(f'{t}/2={n}')
    elif n%2!=0:
        n=3*n+1
        print(f'{t}*3+1={n}')
print('End')

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-11 13.56.09.png](../Pictures/%E6%88%AA%E5%B1%8F/%E6%88%AA%E5%B1%8F2024-10-11%2013.56.09.png)

### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/

思路：

整数到罗马数：位值-对应相应的罗马数字

罗马数到整数：从左到右读取，并对应相应的数值进行加和

##### 代码

```python
n=input()
try:
    n=int(n)
    roma=''
    roma+='M'*(n//1000)
    n%=1000
    baiwei=n//100
    if baiwei==4:
        roma+='CD'
    elif baiwei==9:
        roma+='CM'
    else:roma+='D'*(baiwei//5)+'C'*(baiwei%5)
    n%=100
    shiwei=n//10
    if shiwei==4:
        roma+='XL'
    elif shiwei==9:
        roma+='XC'
    else:roma+='L'*(shiwei//5)+'X'*(shiwei%5)
    n%=10
    if n==4:roma+='IV'
    elif n==9:roma+='IX'
    else:roma+='V'*(n//5)+'I'*(n%5)
    print(roma)
except ValueError:
    arab=0
    duiying={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    while len(n)>=2:
        if n[0:2:] in duiying.keys():
            arab+=duiying[n[0:2:]]
            n=n[2::]
        else:
            arab+=duiying[n[0]]
            n=n[1::]
    if n:arab+=duiying[n[0]]
    print(arab)# 

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-11 14.07.01.png](../../../var/folders/qp/m6q152dj0lq6k8v7bj3xs9br0000gn/T/TemporaryItems/NSIRD_screencaptureui_lW8rqw/%E6%88%AA%E5%B1%8F2024-10-11%2014.07.01.png)

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/

思路：

比第i项大超过d的数：山

比第i项小超过d的数：谷

如果第i项前面有比它大的数：

```
如果第i项i前面没有山或谷：
    把第i项一直往前挪
```

```

else：把第i项挪到它前面那一个数比它小为止
```

结果：TLE。。

代码

```python
n,d=map(int,input().split())
hs=[]
for i in range(n):
    hs.append(int(input()))
i=1
while i <len(hs):
    it=i#cun yi xia i de zhi
    while i>0:
        if hs[i]<max(set(hs[0:i:])) :
            if max(set(hs[0:i:])) - hs[i] <= d and abs(hs[i]-min(set(hs[0:i:])))<=d:
                t=hs[i-1]
                hs[i-1]=hs[i]
                hs[i]=t
                i-=1
            elif hs[i]<hs[i-1] and hs[i-1]-hs[i]<=d:
                t = hs[i - 1]
                hs[i - 1] = hs[i]
                hs[i] = t
                i -= 1
            else:break
        else:break
    i = it + 1

for i in hs:
    print(i)

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

没AC...

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==
（怎么我写了两次而且点了保存这里都没东西...）
今天（14号）把OJ选做清了，之前贪心的题不会，是问AI的，昨晚学了一点，现在能有一点思路了。
感觉要好好学算法了。