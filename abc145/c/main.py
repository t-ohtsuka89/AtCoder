import itertools
import math
import statistics
from typing import Iterable, Tuple


def get_length(start_point: Tuple[int, int], end_point: Tuple[int, int]) -> float:
    x_i, y_i = start_point
    x_j, y_j = end_point
    return math.sqrt(((x_i - x_j) ** 2) + ((y_i - y_j) ** 2))


def get_total_length(path: Tuple[Tuple[int, int]]):
    total_len = 0
    n = len(path)
    for i in range(n - 1):
        total_len += get_length(path[i], path[i + 1])
    return total_len


N = int(input())

coordinate_list = tuple(tuple(map(int, input().split())) for _ in range(N))
total_length_list = [get_total_length(path) for path in itertools.permutations(coordinate_list)]
print(statistics.mean(total_length_list))
