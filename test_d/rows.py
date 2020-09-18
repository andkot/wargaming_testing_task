def row(n):
    if n ==0:
        return 0
    else:
        return 1/n + row(n-1)

for i in range(20):
    print(i, 10*row(i))