'''
WHY CAN'T THE WOODCUTTER FELL THE TREES TOWARDS BEYOND THE ROAD?!!
'''
n=int(input())
tree=[]
qujian=[]
biaoji= []
reversemark={}
for i in range(n):
    x,h=map(int,input().split())
    biaoji.append(x)
    reversemark[x]=i
    tree.append((x-h,x,x,-1))
    tree.append((x,x+h,x,1))
tree.sort(key=lambda x: x[1])
end=0
cut=0
#print(tree)
#print(biaoji)
#print(reversemark)
for i in range(len(tree)):
    adjacentree=biaoji[min(reversemark[tree[i][2]]+tree[i][3],len(biaoji)-1)]
    if tree[i][3]==1:
        no_tree_hindering=adjacentree>tree[i][1] or adjacentree==tree[i][2]
    elif tree[i][3]==-1:
        no_tree_hindering=adjacentree<tree[i][0]
    #print(end,no_tree_hindering)
    if end==0 or (tree[i][0]>end and no_tree_hindering):
        #print(end,tree[i])
        end=tree[i][1]
        cut+=1
print(cut)


