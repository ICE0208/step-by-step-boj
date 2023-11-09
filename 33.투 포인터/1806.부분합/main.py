import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    left, right = 0, 0

    cur_sum = lst[0]
    min_len = N + 1
    while left <= right:
        if cur_sum >= S:
            min_len = min(min_len, right - left + 1)
            cur_sum -= lst[left]
            left += 1
        else:
            right += 1
            if right == N:
                break
            cur_sum += lst[right]

    print(min_len if min_len != N + 1 else 0)
