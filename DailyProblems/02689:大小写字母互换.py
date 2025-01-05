n=list(input())
for i in range(len(n)):
    if n[i]>='a' and n[i]<='z':
        n[i]=n[i].upper()
    elif n[i]>='A' and n[i]<='Z':
        n[i]=n[i].lower()
for i in n:
    print(i,end='')

