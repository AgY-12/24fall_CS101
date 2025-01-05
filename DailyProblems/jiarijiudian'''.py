n=int (input())
count=1
ds=[]
ms=[]
while True :
    try:
        hotel = input().split()
        distance,money=map(int,hotel)
        ds.append(distance)
        ms.append(money)
    except (EOFError,ValueError):
        break

_ = list(zip(ds, ms))
hotels = sorted(_, key=lambda _: _[0])
for i in range(1, n):
    min_money = min(hotels[j][1] for j in range(0, i))
    if hotels[i][1] < min_money:
        count += 1
if _:
    print(count)