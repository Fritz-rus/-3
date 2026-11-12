n = int(input())
s = 0

for i in range(2, n):
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print(i)

    s = 0