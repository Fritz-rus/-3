x = int(input())
c = 0
for i in range(1, x):
    for j in range(i, x):
        if i**2 + j**2 == x:
            c+=1
print(c)