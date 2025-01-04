def compare(a,b):
    if int(a+b)>int(b+a):return '>'
    elif int(a+b)==int(b+a): return '='
    else:return '<'
n=int(input())
nums=list(input().split())
sorted_nums=[nums[0]]
for i in range(1,n):#从大->小
    l,r=0,len(sorted_nums)
    while l<r:
        zz=(l+r)//2
        #print('l,r,zz,nums[i]:', l, r, zz, nums[i])
        #print(sorted_nums)
        if zz==0:
            if compare(sorted_nums[0],nums[i])!='>':
                sorted_nums=[nums[i]]+sorted_nums
                break
        elif compare(sorted_nums[zz-1],nums[i])!='<' and compare(sorted_nums[zz],nums[i])!='>':
            sorted_nums=sorted_nums[0:zz]+[nums[i]]+sorted_nums[zz:]
            #print('insert ed!',sorted_nums)
            break
        elif compare(sorted_nums[zz-1],nums[i])=='<' and zz!=0:
            r=zz-1
        elif compare(sorted_nums[zz],nums[i])=='>' :
            l=zz+1
    else:
        zz=l
        sorted_nums=sorted_nums[0:zz]+[nums[i]]+sorted_nums[zz:]
        #print('inserted!', sorted_nums)
#print(sorted_nums)
print(*sorted_nums,sep='',end=' ')
print(*sorted_nums[-1::-1],sep=''
'''
9=99=999=9999=.....>9999999...98>99999999...97>...900000.....0

'''