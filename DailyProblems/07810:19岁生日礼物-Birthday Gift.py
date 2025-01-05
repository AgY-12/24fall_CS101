n=int(input())
for _ in range(n):
    line=input()
    if '19' in line or int(line)%19==0:
        print('Yes')
    else:
        print('No')