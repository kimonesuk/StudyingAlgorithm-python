n,x = map(int,input().split())
A = list(map(int,input().split()))
output = []
for i in range(0,n):
    if A[i]<x:
        output.append(A[i])
print(" ".join(map(str,output)))
