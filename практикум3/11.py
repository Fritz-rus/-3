l = []
r = int(input())

while r != -1:
    l.append(r)
    r = int(input())

m = l[0]

for i in range(1, len(l)):
    if l[i] > m:
        m = l[i]

print(m)