l = []

for i in range(100,1000):
    if i % 17 == 0:
        l.append(i)

for i in l:
    print(i, end=' ')
print()
print(len(l))