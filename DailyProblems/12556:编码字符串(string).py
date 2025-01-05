string=list(input().lower())
l=[]
t=string.pop(0)
l.append(t)
while string:
    while string and t==string[0]:
        t=string.pop(0)
        l.append(t)
    print('('+t+','+str(len(l))+')',end='')
    l=[]
    if string:
        t=string.pop(0)
        l.append(t)
if len(l)!=0:
    print('('+t+','+str(len(l))+')',end='')