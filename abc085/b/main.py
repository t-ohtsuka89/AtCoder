N = int(input())

d_n = list(set(int(input()) for _ in range(N)))
d_n.sort(reverse=True)

bottom = 101
ans = 0
for d in d_n:
    if d < bottom:
        ans += 1
        bottom = d

print(ans)
