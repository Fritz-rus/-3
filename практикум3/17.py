from math import *

n = int(input())
if n < 2:
    print(n)
else:
    while n > 2:
        print(f"{sqrt(n):.3f}")
        n = sqrt(n)