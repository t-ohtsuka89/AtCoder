N = int(input())

# 開始地点
base_t = 0
base_x = 0
base_y = 0

for i in range(N):
    t, x, y = map(int, input().split())
    # 移動に必要な最小ステップ
    delta_x = abs(base_x - x)
    delta_y = abs(base_y - y)
    min_step = delta_x + delta_y

    # 経過時間
    delta_t = t - base_t

    # 判定
    if min_step > delta_t:
        # 到達不可能
        break
    else:
        # 潰す必要がある時間
        over_step = delta_t - min_step
        if over_step % 2 == 0:
            # 到達可能
            pass
        else:
            # 到達不可能
            break
    base_x = x
    base_y = y
    base_t = t
else:
    print("Yes")
    exit()

print("No")
