import sys

N, Y = map(int, input().split())


for i in range(0, N + 1):
    for j in range(0, N + 1):
        k = N - i - j
        if i + j > N or k < 0:
            continue
        if i * 10000 + j * 5000 + k * 1000 == Y:
            print(f"{i} {j} {k}")
            sys.exit(0)
print(f"{-1} {-1} {-1}")
