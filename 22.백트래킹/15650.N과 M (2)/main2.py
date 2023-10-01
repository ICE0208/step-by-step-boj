import sys

input = sys.stdin.readline


# 이진 트리 방법
def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            print(*lst)
        return

    dfs(n + 1, lst + [n])
    dfs(n + 1, lst)


if __name__ == "__main__":
    N, M = map(int, input().split())

    dfs(1, [])
