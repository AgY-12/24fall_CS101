def canwin(a,b):
    return a//b>=2 or a==b
while True:
    a,b=map(int,input().split())
    if (a,b)==(0,0):break
    i=0
    while True:
        i+=1
        a, b = max(a, b), min(a, b)
        if canwin(a,b):
            if i%2==1:
                print('win')
            else:print('lose')
            break
        else:
            a-=b
            continue