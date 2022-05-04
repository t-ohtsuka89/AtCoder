X = input()
M = int(input())
d = max(map(int, X))


def change_nto10(num, base):
    out = 0
    for i in range(1, len(str(num)) + 1):
        out += int(num[-i]) * (base ** (i - 1))
    return out


def is_ok(arg):
    return change_nto10(X, arg) <= M


def meguru_bisect(ng, ok):
    ans = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

if len(X) == 1:
    ans = 1 if int(X) <= M else 0
else:
    ans = meguru_bisect(10**18 + 1, d) - d

print(ans)
