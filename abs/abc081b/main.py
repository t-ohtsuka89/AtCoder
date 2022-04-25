n = input()
a_n = list(map(int, input().split(" ")))

ans = float("inf")

for a in a_n:
    ans = min(ans, len(bin(a)) - bin(a).rfind("1") - 1)
print(ans)
