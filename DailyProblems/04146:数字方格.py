def main():
    n=int(input())
    t=3*n-(3*n)%5
    while True:
        for a in range(0,n+1):
            for c in range(0,n+1):
                if (t-a)%2==0 and (t-c)%3==0 and 0<=t-a-c<=n:
                    print(t)
                    return
        else:t-=5
if __name__=='__main__':
    main()

