N = int(input())
a_n = list(map(int, input().split()))

# 得点の高い順にソート
a_n.sort(reverse=True)

alice = 0
bob = 0

for i in range(N):
    point = a_n[i]
    if i % 2 == 0:
        alice += point
    else:
        bob += point
print(alice - bob)
