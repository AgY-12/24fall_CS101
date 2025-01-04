a=int(input())
b=list(bin(a).lstrip('0b'))
d=b[:]
b.reverse()
if b==d:
    print('Yes')
else:
    print('No')

