n=int(input())
nums=list(input().split())
nums=[(i,int(i)/(10**len(i)-1)) for i in nums]
nums.sort(key=lambda x:x[1],reverse=True)
for i in nums:print(i[0],end='')
print(' ',end='')
for i in nums[::-1]:print(i[0],end='')