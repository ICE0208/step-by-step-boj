import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    list = sorted(list(map(int, input().split())))

    left, right = 0, N - 1
    result = (float("inf"), 0, 0)
    while left < right:
        cur = list[left] + list[right]

        # 특성값 업데이트
        if abs(cur) < abs(result[0]):
            result = (cur, list[left], list[right])

        # left or right 업데이트
        if cur > 0:
            right -= 1
        else:
            left += 1

    print(result[1], result[2])
