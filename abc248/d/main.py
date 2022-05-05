import bisect
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = defaultdict(list)
for i, v in enumerate(A):
    d[v].append(i + 1)

for _ in range(Q):
    L, R, X = map(int, input().split())
    lcount = bisect.bisect_left(d[X], L)
    rcount = bisect.bisect_right(d[X], R)

    print(rcount - lcount)
