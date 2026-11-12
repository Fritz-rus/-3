pr = 0
c = 0
while True:
    n = float(input())
    if n == 0:
        break
    else:
        if n < pr:
            c += 1
    pr = n

print(c)