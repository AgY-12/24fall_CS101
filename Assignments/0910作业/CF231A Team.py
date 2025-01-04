n=input()
n=int(n)
s=0
for i in range(n):
    x,y,z=map(int,input().split())
    if x+y+z>=2:
        s+=1
print(s)