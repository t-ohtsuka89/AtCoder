N = int(input())
A_N = list(map(lambda x: format(int(x), "b"), input().split()))

print(min(map(lambda A: len(A) - 1 - A.rfind("1"), A_N)))
