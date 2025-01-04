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