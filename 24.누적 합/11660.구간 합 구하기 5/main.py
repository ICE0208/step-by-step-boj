import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    lst = [[0 for _ in range(N + 1)]]
    for _ in range(N):
        lst.append([0] + list(map(int, input().split())))

    dp = [[0 for i in range(N + 1)] for j in range(N + 1)]

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            dp[x][y] = lst[x][y] + dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1]

    for test_case_i in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
        print(result)
