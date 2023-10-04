import sys

input = sys.stdin.readline


def bt(n: int, s: int):
    if n == M:
        print(*arr)
        return

    for i in range(s, N + 1):
        arr[n] = i
        bt(n + 1, i)


if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = [0] * M
    bt(0, 1)
