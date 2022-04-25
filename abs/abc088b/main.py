N = int(input())
a_n = list(map(int, input().split()))


a_n = sorted(a_n)
ans = abs(sum(a_n[0::2]) - sum(a_n[1::2]))
print(ans)
