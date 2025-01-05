import math
haab={'pop':1, 'no':2, 'zip':3, 'zotz':4, 'tzec':5, 'xul':6, 'yoxkin':7,
      'mol':8, 'chen':9, 'yax':10, 'zac':11, 'ceh':12, 'mac':13, 'kankin':14,
      'muan':15, 'pax':16, 'koyab':17, 'cumhu':18,'uayet':19}
tzolkin={1:'imix', 2:'ik', 3 :'akbal', 4 :'kan', 5 :'chicchan',6:'cimi',7:'manik',
 8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',13:'ben',14:'ix',15:'mem',16:'cib'
 ,17:'caban',18:'eznab',19:'canac',0:'ahau'
 }
print(n:=int(input()))
for i in range(n):
    nodh,mh,yh=input().split()
    nodh=int(nodh[0:-1:])
    yh=int(yh)
    d=yh*365+(haab[mh]-1)*20+nodh+1
    yt=math.ceil(d/260)-1
    d%=260
    mt=d%20
    dt=d%13
    if dt==0:dt=13
    print(f'{dt} {tzolkin[mt]} {yt}')

