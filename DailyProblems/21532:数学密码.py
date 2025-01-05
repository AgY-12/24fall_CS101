x=int(input())
t=x
j=0
for i in range(6,max(int(x**0.5)+1,8),1):
    if x%i==0:
        j=i
        x=i
        print(int(t/x))
        break
if x!=j:
    for j in range(5,0,-1):
        if x%j==0:
            x=int(x/j)
            print(j)
            break
