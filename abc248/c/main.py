from typing import List

MOD = 998244353
N, M, K = map(int, input().split())

dp = [[0] * K for _ in range(N)]
for i in range(M):
    dp[0][i] = 1

for i in range(N - 1):
    for j in range(K):
        if dp[i][j] != 0:
            for d in range(1, M + 1):
                if j + d >= K:
                    break
                dp[i + 1][j + d] += dp[i][j]
                dp[i + 1][j + d] %= MOD
print(sum(dp[N - 1]) % MOD)
