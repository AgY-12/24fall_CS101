n=int(input())
a=bin(n)[2:]
b=a[-1::-1]
if a==b:print('Yes')
else:print('No')