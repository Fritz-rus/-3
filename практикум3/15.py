N = int(input())
n = [i for i in range(1, N+1)]
for i in n:
    if i <= 1:
        continue

    p = True
    for j in range(2, i):
        if i % j == 0:
            p = False
            break

    if p:
        print(i)
