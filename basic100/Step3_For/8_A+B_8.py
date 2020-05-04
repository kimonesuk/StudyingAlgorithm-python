t = int(input())
a = []
b = []
for i in range(1,t+1):
    alpha,beta = map(int,input().split())
    a.append(alpha)
    b.append(beta)
for i in range(0, t):
    num = i+1
    sum = a[i]+b[i]
    print(f'Case #{num}: {a[i]} + {b[i]} = {sum}')
