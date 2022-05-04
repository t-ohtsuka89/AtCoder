import re

S = input()

if re.fullmatch(r"(dream|dreamer|erase|eraser)*", S):
    print("YES")
else:
    print("NO")
