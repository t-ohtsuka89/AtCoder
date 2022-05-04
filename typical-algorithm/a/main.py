N, K = map(int, input().split())
a_n = list(map(int, input().split()))


def is_ok(arg):
    return a_n[arg] >= K


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


if not max(a_n) >= K:
    print(-1)
    exit()
print(meguru_bisect(ng=-1, ok=N))
