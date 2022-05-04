import bisect

N = int(input())
L_N = sorted(list(map(int, input().split())))

ans = 0
for i in range(2, N):
    for j in range(1, i):
        ans += max(0, j - bisect.bisect_right(L_N, L_N[i] - L_N[j]))

print(ans)
