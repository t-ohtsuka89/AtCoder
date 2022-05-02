from typing import List

N, M = map(int, input().split())

switch_info_list: List[List[int]] = []

for i in range(M):
    switch_info_list.append(list(map(int, input().split())))
p_list = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    # スイッチのON, OFFパターン
    pattern = format(i, f"0{N}b")
    assert len(pattern) == N
    on_light_num = 0
    # 各電球の状態チェック
    for j in range(M):
        switch_num = switch_info_list[j][0]
        switches = switch_info_list[j][1:]
        p = p_list[j]
        on_switch_num = 0
        for switch in switches:
            on_switch_num += int(pattern[switch - 1])
        if on_switch_num % 2 == p:
            on_light_num += 1
    if on_light_num == M:
        ans += 1


print(ans)
