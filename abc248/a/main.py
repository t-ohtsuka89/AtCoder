S = list(map(int, input()))

for i in range(10):
    if not i in S:
        print(i)
        exit()
