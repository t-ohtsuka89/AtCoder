N = int(input())

base_x = 0
base_y = 0
base_t = 0

for _ in range(N):
    t, x, y = map(int, input().split())
    t_d = abs(t - base_t)
    x_d = abs(x - base_x)
    y_d = abs(y - base_y)

    min_step = x_d + y_d
    if min_step > t_d or (t_d - min_step) % 2 != 0:
        print("No")
        exit(0)
    else:
        base_x = x
        base_y = y
        base_t = t

print("Yes")
