N, M = map(int, input().split())

s_c_list = {tuple(map(int, input().split())) for _ in range(M)}

for i in range(10 ** (N - 1), 10**N):
    # 桁数Nを最小値から探索
    target = list(map(int, str(i)))
    for s_i, c_i in s_c_list:
        # 各条件の確認
        if target[s_i - 1] != c_i:
            break
    else:
        # 全部OK
        print(i)
        exit()
print(-1)
