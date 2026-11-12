s = input()
n_s = ''
if len(s) < 3:
    print(s)
else:
    for i in range(2,len(s)+1, 3):
        n_s += s[i]
print(n_s)