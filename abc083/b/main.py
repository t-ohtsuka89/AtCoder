N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    total = sum(map(int, str(i)))
    if total >= A and total <= B:
        ans += i
print(ans)
