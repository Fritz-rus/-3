n = int(input())
k = 0
p = 1 #кол-во цепочек ответов
while p < n:
    p *= 2
    k += 1
print(k)