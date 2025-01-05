n=int(input())
sum=0
for i in range(n):
    line=input().split('###')
    if line[0]=='':
        while '' in line:
            line.remove('')
        if len(line)%2==0:
            sum+=int(len(line)/2)-line.count(' ')
        else:
            sum+=int(len(line)/2)+1-line.count(' ')
    else:
        sum += int(len(line) / 2)  - line.count(' ')
print(sum)