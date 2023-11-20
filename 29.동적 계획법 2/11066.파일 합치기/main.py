import sys

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        lst = [0] + list(map(int, input().split()))
        sum_lst = [0 for i in range(k + 1)]
        for i in range(1, k + 1):
            sum_lst[i] = sum_lst[i - 1] + lst[i]
        dp = [[float("inf") for i in range(k + 1)] for j in range(k + 1)]

        for size in range(1, k + 1):
            for i in range(1, k + 1):
                j = i + size - 1
                if j > k:
                    break
                if i == j:
                    dp[i][j] = 0
                    continue

                for m in range(i, j + 1):
                    if m == j:
                        dp[i][j] = min(dp[i][j], dp[i][m] + sum_lst[j] - sum_lst[i - 1])
                        continue
                    dp[i][j] = min(
                        dp[i][j], dp[i][m] + dp[m + 1][j] + sum_lst[j] - sum_lst[i - 1]
                    )
        print(dp[1][k])
