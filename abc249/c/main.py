import collections

N, K = map(int, input().split())
A = [input() for _ in range(N)]


num_list = []
for i in range(1 << N):
    selected_strings = "".join([A[j] for j in range(N) if i >> j & 1])
    char_counter = collections.Counter(selected_strings)
    key_count = sum(1 for _ in filter(lambda items: items[1] == K, char_counter.items()))
    num_list.append(key_count)

print(max(num_list))
