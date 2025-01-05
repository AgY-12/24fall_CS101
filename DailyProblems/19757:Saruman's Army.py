'''
r=5
distance:
1 6 5 3 5 7 8 3 4 8 5
army:
(1 2) (8 13 16) (21) (28) (36 39 43) (51 56)
'''
while True:
    r,n=map(int,input().split())
    if (r,n)==(-1,-1):break
    army=list(map(int,input().split()))
    army.sort()
    count=0
    i=0
    while i <len(army):
        j=1
        while (j+i)<len(army) and army[i+j]-army[i]<=r:
           j+=1
        i=i+j-1
        j = 1
        while (j+i) < len(army) and army[i + j] - army[i] <= r:
            j += 1
        i = i + j
        count+=1
    print(count)
