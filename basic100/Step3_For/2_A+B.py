t = int(input())
a = [], b = []
for i in range(1,t+1):
    alpha,beta = map(int,input().split())
    a.append(alpha)
    b.append(beta)
for i in range(0, t):
    print(a[i]+b[i])
