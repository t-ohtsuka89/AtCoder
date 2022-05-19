import sys

sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
T_BOARD = [list(input()) for _ in range(H)]

start_row = None
start_column = None

# get start pos
for row in range(H):
    for column in range(W):
        if T_BOARD[row][column] == "s":
            start_row, start_column = row, column
            break

assert start_row is not None
assert start_column is not None


def is_valid(row: int, column: int) -> bool:
    if row < 0 or row >= H:
        return False
    if column < 0 or column >= W:
        return False
    return True


def dfs(row: int, column: int):
    # out of range
    if not is_valid(row, column):
        return
    # is wall
    if T_BOARD[row][column] == "#":
        return

    if T_BOARD[row][column] == "g":
        print("Yes")
        exit()

    T_BOARD[row][column] = "#"
    dfs(row - 1, column)
    dfs(row, column - 1)
    dfs(row, column + 1)
    dfs(row + 1, column)


dfs(start_row, start_column)
print("No")
