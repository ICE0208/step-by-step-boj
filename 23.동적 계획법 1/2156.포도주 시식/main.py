import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    wine = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        wine[i] = int(input())

    dp = [0 for _ in range(n + 1)]
    dp[1] = wine[1]
    if n >= 2:
        dp[2] = wine[1] + wine[2]
    if n >= 3:
        dp[3] = max(dp[2], wine[2] + wine[3], dp[1] + wine[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

    print(dp[n])
