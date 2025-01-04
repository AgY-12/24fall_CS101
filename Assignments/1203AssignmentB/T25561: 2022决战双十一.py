n,m=map(int,input().split())
goods=[]
for i in range(n):
    goods.append({})
    line=list(input().split())
    for _ in line:
        k,v=map(int,_.split(':'))
        goods[i][k]=v
coupons={}
for i in range(1,m+1):
    coupons[i]={}
    line=input().split()
    for _ in line:
        k,v=map(int,_.split('-'))
        coupons[i][k]=v
stores=[list(goods[i].keys()) for i in range(n)]
shopping_list=[0 for i in range(n)]
shopping_lists=[]

def buy(goods_id):
    global shopping_list,shopping_lists
    if goods_id==n:
        shopping_lists.append(shopping_list[:])
    else:
        for i in range(len(stores[goods_id])):
            shopping_list[goods_id]=i
            buy(goods_id+1)
        shopping_list[goods_id]=0

buy(0)


ans=float('inf')
for shopping_list in shopping_lists:
    anstmp = 0
    calc = [[] for _ in range(m + 1)]
    for i in range(len(shopping_list)):
        calc[stores[i][shopping_list[i]]].append(goods[i][stores[i][shopping_list[i]]])
    '''
    print('calc:')
    for _ in calc:
        print(*_)
    '''
    cutoff=[]
    for i in range(1,m+1):
        subtract=0
        s=sum(calc[i])
        '''
        print(f'stores:')
        for j in stores:
            print(*j)
        print('shopping_list:')
        print(shopping_list)
        '''
        for man,jian in coupons[i].items():
            if man<=s and jian >subtract:
                subtract=jian
                #print(f'店{i},满{man},{s}-{subtract}')
        cutoff.append(subtract)
        anstmp+=s

    anstmp-=50*(anstmp//300)
    for sub in cutoff:
        anstmp-=sub
    #print('钱:',anstmp)
    ans=min(anstmp,ans)
print(ans)



'''
4 5
1:100 3:130 4:100
3:200 5:100
2:400 3:400 4:410
1:10 5:20
110-10
200-30
300-90 500-91 600-99
400-40 500-51
900-9
'''


