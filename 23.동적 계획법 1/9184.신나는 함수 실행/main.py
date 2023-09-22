import sys

input = sys.stdin.readline

dict = {}  # (a, b, c) : n


def s(a, b, c):
    if (a, b, c) in dict:
        return dict[(a, b, c)]

    result = 0
    if a <= 0 or b <= 0 or c <= 0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = s(20, 20, 20)
    elif a < b and b < c:
        result = s(a, b, c - 1) + s(a, b - 1, c - 1) - s(a, b - 1, c)
    else:
        result = (
            s(a - 1, b, c)
            + s(a - 1, b - 1, c)
            + s(a - 1, b, c - 1)
            - s(a - 1, b - 1, c - 1)
        )

    dict[(a, b, c)] = result
    return result


if __name__ == "__main__":
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1:
            break
        print(f"w({a}, {b}, {c}) = {s(a, b, c)}")
