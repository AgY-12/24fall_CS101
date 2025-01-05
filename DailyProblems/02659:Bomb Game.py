a,b,k=map(int,input().split())#a,r,y是行，b,x,c是列
psb={(x,y) for x in range(1,a+1) for y in range(1,b+1)}
for i in range(k):
    r,c,d,t=map(int,input().split())
    p=(d-1)//2
    psb_tmp=set()
    impsb_tmp=set()
    if t==1:
        for y in range(r-p,r+p+1):
            for x in range(c-p,c+p+1):
                psb_tmp.add((y,x))
        psb=psb.intersection(psb_tmp)
    elif t==0:
        for y in range(r-p,r+p+1):
            for x in range(c-p,c+p+1):
                impsb_tmp.add((y,x))
        psb=psb-impsb_tmp
print(len(psb))

'''
da dao de qu jiao ji ,ba da dao de ge zi zuo ji he 
mei da dao de qu bing ji , zuo jian ji
'''