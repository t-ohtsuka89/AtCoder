A, B, X = map(int, input().split())


def is_ok(arg):
    return A * arg + B * len(str(arg)) <= X


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(10**9 + 1, 0))
