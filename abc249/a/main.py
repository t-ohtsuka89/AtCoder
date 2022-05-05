A, B, C, D, E, F, X = map(int, input().split())

takahashi = 0
aoki = 0

for i in range(X):
    v_t = i % (A + C)
    v_a = i % (D + F)
    if v_t < A:
        takahashi += B
    if v_a < D:
        aoki += E

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
