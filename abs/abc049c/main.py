import re

S = input()

print("NO" if re.compile(r"(dream|dreamer|erase|eraser)*").fullmatch(S) is None else "YES")
