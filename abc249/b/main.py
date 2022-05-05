import re

S = input()


def cond1(text: str):
    return False if re.search(r"[A-Z]", text) is None else True


def cond2(text: str):
    return False if re.search(r"[a-z]", text) is None else True


def cond3(text: str):
    return len(text) == len(set(text))


if cond1(S) and cond2(S) and cond3(S):
    print("Yes")
else:
    print("No")
