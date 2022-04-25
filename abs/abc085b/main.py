N = int(input())
a_n = [int(input()) for _ in range(N)]
print(len(set(sorted(a_n))))
