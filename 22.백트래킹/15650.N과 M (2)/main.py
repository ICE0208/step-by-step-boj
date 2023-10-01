import sys

input = sys.stdin.readline


def backtrack(n):
    if n == M:
        print(*arr)
        return

    start = 1 if n == 0 else arr[n - 1] + 1
    for i in range(start, N + 1):
        arr[n] = i
        backtrack(n + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [-1] * M

    backtrack(0)
