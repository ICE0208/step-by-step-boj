import sys

input = sys.stdin.readline


def recur(n, r_start, c_start):
    if n == 1:
        arr[r_start][c_start] = "*"
        return

    child_n = n // 3
    for r_offset in range(0, 3):
        for c_offset in range(0, 3):
            if r_offset == 1 and c_offset == 1:
                continue
            recur(child_n, r_start + child_n * r_offset, c_start + child_n * c_offset)


if __name__ == "__main__":
    N = int(input())

    arr = [[" " for i in range(N + 1)] for j in range(N + 1)]

    recur(N, 1, 1)

    for r in range(1, N + 1):
        print("".join(arr[r][1:]))
