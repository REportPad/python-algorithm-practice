n,m=map(int, input().split())
ret = -1
for i in range(n):
    data = list(map(int, input().split()))
    dmin = min(data)
    ret = max(ret, dmin)
    
print(ret)
