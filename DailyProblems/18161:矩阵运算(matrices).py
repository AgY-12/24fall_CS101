A,B,C=[],[],[]
def matcheng(A,B):
    if A[0][1]==B[0][0]:
        D=[]
        for i in range(A[0][0]):
            D.append([])
            for j in range(B[0][1]):
                D[i].append(0)
                for k in range(A[0][1]):
                    D[i][j]+=A[i+1][k]*B[k+1][j]
        return D
def matjia(B,C):
    if B[0][0]==C[0][0] and B[0][1]==C[0][1]:
        E=[]
        for i in range(B[0][0]):
            E.append([])
            for j in range(C[0][1]):
                E[i].append(B[i+1][j]+C[i+1][j])
        return E
x,y=map(int,input().split())
A.append([x,y])
for i in range(x):
    line=list(map(int,input().split()))
    A.append(line)
x,y=map(int,input().split())
B.append([x,y])
for i in range(x):
    line=list(map(int,input().split()))
    B.append(line)
x,y=map(int,input().split())
C.append([x,y])
for i in range(x):
    line=list(map(int,input().split()))
    C.append(line)
D=matcheng(A,B)
try:
    D.insert(0,[len(D),len(D[0])])
    Ans=matjia(D,C)
    for i in Ans:
        print(' '.join(map(str,i)))
except AttributeError:print('Error!')
except TypeError:print('Error!')