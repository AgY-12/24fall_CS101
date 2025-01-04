from functools import lru_cache

S=0
CHS=0
def dfs(x):
    global S
    S+=1
    print(f'x:{x},S:{S}')
    if x==1:
        return 1
    return x+dfs(x-1)

@lru_cache(maxsize=None)
def chdfs(x):
    global CHS
    CHS+=1
    print(f'x:{x},CHS:{CHS}')
    if x==1:
        return 1
    return x+chdfs(x-1)

for i in range(1,11):
    print(dfs(i))
print(S)
print('-------')
for i in range(1,11):
    print(chdfs(i))
print(CHS)
'''
chdfs在算chdfs(3)的时候，
因为已经算过了chdfs(2)，
就直接搬出了它存的chdfs(2)的值，
不会再跑一遍chdfs(2)，
所以里面的全局变量CHS也不会相应更新
是故带lru_cache的递归不能在里面弄全局变量
'''