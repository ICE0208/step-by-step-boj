import sys

input = sys.stdin.readline

# Bottom-Up
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [-1001] * 1000000
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    result = max(dp)
    print(result)
