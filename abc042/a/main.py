from collections import Counter

c = Counter(input().split())
if c["5"] == 2 and c["7"] == 1:
    print("YES")
else:
    print("NO")
