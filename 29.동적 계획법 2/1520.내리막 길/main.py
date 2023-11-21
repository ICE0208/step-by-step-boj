import sys

input = sys.stdin.readline

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    enable_path = 0
    if r == M - 1 and c == N - 1:
        return 1

    for move in moves:
        next_r = r + move[0]
        next_c = c + move[1]
        if next_r < 0 or next_c < 0 or next_r >= M or next_c >= N:
            continue

        cur_height = lst[r][c]
        next_height = lst[next_r][next_c]
        if next_height >= cur_height:
            continue

        enable_path += dfs(next_r, next_c)

    dp[r][c] = enable_path
    return dp[r][c]


if __name__ == "__main__":
    M, N = map(int, input().split())

    lst = []
    for _ in range(M):
        lst.append(list(map(int, input().split())))

    dp = [[-1 for i in range(N)] for j in range(M)]

    result = dfs(0, 0)
    print(result)
