from itertools import product

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]


def is_ok(mid):
    s = set()
    for a in ability:
        s.add(sum(1 << i for i in range(5) if a[i] >= mid))
    for x, y, z in product(s, repeat=3):
        if x | y | z == 31:
            return True
    return False


def binary_search(ok, ng):
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = binary_search(0, 10**9 + 1)
print(ans)
