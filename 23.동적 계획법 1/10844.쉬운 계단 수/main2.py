import sys

input = sys.stdin.readline

DIVIDE = 1000000000


def k(dep, cur):
    global N, dp, DIVIDE
    if dep == N:
        return 1
    if dp[dep][cur] != 0:
        return dp[dep][cur]

    if 1 <= cur <= 8:
        dp[dep][cur] = (k(dep + 1, cur - 1) + k(dep + 1, cur + 1)) % DIVIDE
    elif cur == 0:
        dp[dep][cur] = k(dep + 1, 1) % DIVIDE
    else:
        dp[dep][cur] = k(dep + 1, 8) % DIVIDE
    return dp[dep][cur]


if __name__ == "__main__":
    N = int(input())

    dp = [[0 for i in range(10)] for j in range(N + 1)]

    sum = 0
    for i in range(1, 10):
        sum = (sum + k(1, i)) % DIVIDE
    print(sum)
