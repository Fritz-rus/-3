n = int(input())
t = 1
l = []
while t ** 3 <= n:
    l.append(t**3)
    t+=1

for i in l:
    print(i, end=' ')