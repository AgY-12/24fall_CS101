while True:
    n=int(input())
    if n!=0:
        hotel=[]
        best=[10001,10001,0]
        num=0
        for i in range(n):
            d,c=map(int,input().split())
            hotel.append([d,c])
        hotel.sort()
        best=hotel[0]
        i=0
        num=1
        while i<len(hotel):
            try:
                while hotel[i][0]==best[0]:
                    i+=1#走到下一个‘D'
            except IndexError:break
            if hotel[i][1]<best[1]:
                num+=1
                best=hotel[i]
            else:i+=1
        print(num)
    else:break
'''15
3 1
4 1
5 1
6 1
2 2
4 2
1 3
3 3
6 3
2 4
3 4
4 4
5 4
1 5
6 5
15
2 6
234 536
234 634
143 764
234 7674
12 7647
324 422
123 644
111 333
333 444
111 555
222 555
553 666
223 542
234 654'''