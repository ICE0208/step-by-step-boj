import sys

input = sys.stdin.readline


def backtrack(n, lst):
    if n == M:
        print(*lst)
        return

    for i in range(1, N + 1):
        if visited[i] == True:
            continue

        visited[i] = True
        backtrack(n + 1, lst + [i])
        visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [False] * (N + 1)

    backtrack(0, [])
