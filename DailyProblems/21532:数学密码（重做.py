

x=int(input())
for i in range(6,x+1):
    if x%i==0 :
        print(x//i)
        break
'''
x=int(input())
for i in range(int(x/3),0,-1):
    if x%i==0 and int(x//i)>=6:
        print(i)
        break        
'''
'''一个快一个慢是数据的问题'''