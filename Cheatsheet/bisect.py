def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if hi==None:
        hi=len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    else:
         while lo < hi:
             mid = (lo + hi) // 2
             if key(a[mid]) < key(x):
                 lo = mid + 1
             else:
                hi = mid
    return lo
def bisect_right(a, x, lo=0, hi=None, *, key=None):
    if hi==None:
        hi=len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
    else:
         while lo < hi:
             mid = (lo + hi) // 2
             if key(a[mid]) < key(x):
                 lo = mid + 1
             else:
                hi = mid
    return lo
a=[1,2,3,3,3,3,3,3,3,6,7]
x=3
print(bisect_left(a, x))