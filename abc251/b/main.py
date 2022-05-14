import bisect
import copy
import itertools
from typing import List

N, W = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(1, 4):
    for pattern in itertools.combinations(range(N), i):
        if i != 1 and pattern.count(pattern[0]) == len(pattern):
            # 同じ錘は使わない
            continue

good_nums = set()
ans = 0
# 1つ選ぶ
left = bisect.bisect_left(A, W)
good_nums |= set(A[:left])

# 2つ選ぶ
for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            good_nums.add(A[i] + A[j])

# 3つ選ぶ
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            total = A[i] + A[j] + A[k]
            if total <= W:
                good_nums.add(total)

print(len(good_nums))
