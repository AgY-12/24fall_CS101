n=int(input())
stairs=[1,1]+[0]*n
for i in range(2,n+1):
    stairs[i]=stairs[i-1]+stairs[i-2]
print(stairs[n])