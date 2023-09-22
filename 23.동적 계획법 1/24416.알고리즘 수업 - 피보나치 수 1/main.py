import sys

input = sys.stdin.readline


def fib(n):
    # dp를 위한 리스트 : dp[1] = dp[2] = 1, len == n+1
    dp = [None, 1, 1] + [0] * (n - 2)

    # dp를 이용하여 피보나치 수 구하기
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib2(n):
    return n - 2


if __name__ == "__main__":
    # N 입력 받기
    N = int(input())

    print(fib(N), fib2(N))
