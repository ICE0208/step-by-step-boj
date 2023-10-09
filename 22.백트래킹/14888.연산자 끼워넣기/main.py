import sys

input = sys.stdin.readline


def operate(n, result, opers_cnt, operator):
    if opers_cnt[operator] > 0:
        opers_cnt[operator] -= 1
        if operator == 0:  # +
            bt(n + 1, result + nums[n], opers_cnt)
        elif operator == 1:  # -
            bt(n + 1, result - nums[n], opers_cnt)
        elif operator == 2:  # x
            bt(n + 1, result * nums[n], opers_cnt)
        elif operator == 3:  # /
            bt(n + 1, int(result / nums[n]), opers_cnt)
        opers_cnt[operator] += 1


def bt(n, result, opers_cnt):
    global max_result, min_result
    if n == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    for operator in range(4):
        operate(n, result, opers_cnt, operator)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    opers_cnt = list(map(int, input().split()))

    max_result, min_result = float("-inf"), float("inf")
    bt(1, nums[0], opers_cnt)

    print(max_result, min_result, sep="\n")
