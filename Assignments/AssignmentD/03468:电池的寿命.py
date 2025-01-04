import sys
lines=sys.stdin.read().splitlines()
id=0
while id<len(lines):
    n=int(lines[id])
    id=id+1
    batteries=list(map(int,lines[id].split()))
    id+=1
    m=max(batteries)
    s=sum(batteries)
    if 2*m>s:
        print('%.1f'%(s-m))
    else:
        print('%.1f'%(s/2))
