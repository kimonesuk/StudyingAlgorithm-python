import sys
t = int(input())
a = []
b = []
for i in range(1,t+1):
    alpha,beta = map(int,sys.stdin.readline().split())
    a.append(alpha)
    b.append(beta)
for i in range(0, t):
    print(a[i]+b[i])
