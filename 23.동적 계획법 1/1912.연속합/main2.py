import sys

# RecursionError 빙지
sys.setrecursionlimit(100002)

input = sys.stdin.readline


# Top-Down
def recur(k):
    if dp[k] != None:
        return dp[k]

    dp[k] = max(recur(k - 1) + arr[k], arr[k])
    return dp[k]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [None for _ in range(n)]
    dp[0] = arr[0]

    recur(n - 1)
    answer = max(dp)

    print(answer)
