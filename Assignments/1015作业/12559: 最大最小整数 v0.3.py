import bisect
rt=''
unsorted=[]
def greedysort(n):
    global rt
    global unsorted
    minl = min(len(_) for _ in n)
    n.sort()
    print(n)
    print('minl:',minl)
    # 取出最前面的位相同的数们
    print(n[0][0:minl])
    cut=bisect.bisect_right(n, n[0][0:minl],key=lambda x:x[0:minl])
    print(cut)
    sorttmp = n[0:cut]
    print('l;sorttmp:',len(sorttmp),sorttmp)
    i=0
    rt+=sorttmp[0][0:minl]
    print('rt:',rt)
    while i < len(sorttmp):
        sorttmp[i]=sorttmp[i][minl:]#砍去不用再比较的头
        if sorttmp[i]=='':
            del(sorttmp[i])
            continue
        else:i+=1
    unsorted += n[cut::]
    print('unsorted',unsorted)
    print('cleared!',sorttmp)
    if len(sorttmp)>1:
        rt+=greedysort(sorttmp)
        print('rt:',rt,'unsorted:',unsorted)
    else:
        rt+=sorttmp[0]
        print('rt:', rt, 'unsorted:', unsorted)
    greedysort(unsorted)
    return rt

n=int(input())
nums=list(input().split())
greedysort(nums)
'''
898965 89896 8989 898 89 84 823 8 76 777 75 7 
89896 

8 
89 898 8987 89876 87 876 8765 87654
'''

