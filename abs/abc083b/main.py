N, A, B = list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    tmp = sum(map(int, str(i)))
    if A <= tmp and tmp <= B:
        ans += i
print(ans)
