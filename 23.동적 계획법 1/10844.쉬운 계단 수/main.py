import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    MOD = 1000000000

    dp = [[0 for i in range(10)] for j in range(101)]
    for i in range(1, 10):  # 0은 포함 X
        dp[1][i] = 1

    for i in range(2, N + 1):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = (dp[i - 1][1]) % MOD
            elif j == 9:
                dp[i][j] = (dp[i - 1][8]) % MOD
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

    sum = 0
    for i in range(0, 10):
        sum = (sum + dp[N][i]) % MOD
    print(sum)
