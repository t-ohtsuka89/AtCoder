N = int(input())
origins = set()
points = list()


def is_original(S: str):
    return S not in origins


max_point = 0
ans = 0
for i in range(N):
    S, T = input().split()
    if S in origins:
        continue
    T = int(T)
    if T > max_point:
        ans = i + 1
        max_point = T
    origins.add(S)

print(ans)
