n, k, r = map(int, input().split())
c = 1
while n < r:
    n = n + (n*k)//100
    c += 1
print(c)