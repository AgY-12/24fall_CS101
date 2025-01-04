H,L,n=map(int,input().split())
g=10
v=list(map(float,input().split()))
v.sort()
vmid=v[n//2]
h=H-(g*L**2)/(2*vmid**2)
print('{:.2f}'.format(h))