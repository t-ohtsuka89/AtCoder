N = int(input())

for X in range(46300):
    if int(X * 1.08) == N:
        print(X)
        exit()
else:
    print(":(")
