from itertools import product

H, W = map(int, input().split())
BOARD = [list(input()) for _ in range(H)]


def get_bomb_count(row: int, column: int) -> int:
    count = 0
    for dx, dy in product(range(-1, 2), repeat=2):
        try:
            count += 1 if BOARD[row + dx][column + dy] == "#" else 0
        except IndexError:
            count += 0
    return count


# for i in range(H):
#     for j in range(W):
for i, j in product(range(H), range(W)):
    if BOARD[i][j] == ".":
        BOARD[i][j] = str(get_bomb_count(i, j))
for i in range(H):
    print("".join(BOARD[i]))
