#打素数表
import math
'''
def print_sushubiao():
    sushubiao=[]
    temp=1
    for i in range(3,2000,2):
        for j in range(2,int(math.sqrt(i)+3)):
            temp=j
            if i%j==0:
                break
        if temp==int(math.sqrt(i)+2):
            sushubiao.append(i)
        temp=1
    return sushubiao
    #打素数表太费空间！
'''
def find_factorial(n):
    if n >=4 and n%2==0:return True
    else:
        for i in range(3,int(math.sqrt(n))+1):
            if n%i==0:
                return True
        return False
#正式开始
'''
ssb=print_sushubiao()
x=int(input())
if x>=6 and x%2==0:
    for y in ssb[0:min(int(x/2),len(ssb)-1)]:
        if x-y in ssb and y<=x-y:
            print(str(x)+'='+str(y)+'+'+str(x-y))
else:print('Error!')
'''
x=int(input())
if x>=6 and x%2==0:
    for y in range(3,int(x/2)+1,2):
        if find_factorial(y) == False and find_factorial(x-y)==False:
            print(str(x)+'='+str(y)+'+'+str(x-y))
else:print('Error!')