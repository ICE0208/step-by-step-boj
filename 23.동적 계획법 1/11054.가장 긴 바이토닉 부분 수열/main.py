import sys

input = sys.stdin.readline


def find_replace_index(lst, num):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = l + (r - l) // 2
        if lst[mid] >= num:
            r = mid
        else:
            l = mid + 1
    return r


def find_replace_index2(lst, num):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = l + (r - l) // 2
        if lst[mid] <= num:
            r = mid
        else:
            l = mid + 1
    return r


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0

    for center in range(0, N):
        center_num = arr[center]

        left_count = 0
        stack = []
        for i in range(0, center):
            # 왼쪽 부분 구하기
            if arr[i] >= center_num:
                continue
            if not stack or stack[-1] < arr[i]:
                stack.append(arr[i])
                left_count += 1
                continue
            stack[find_replace_index(stack, arr[i])] = arr[i]

        right_count = 0
        stack2 = []
        for i in range(center + 1, N):
            # 오른쪽 부분 구하기
            if arr[i] >= center_num:
                continue
            if not stack2 or stack2[-1] > arr[i]:
                stack2.append(arr[i])
                right_count += 1
                continue
            stack2[find_replace_index2(stack2, arr[i])] = arr[i]

        result = max(result, left_count + right_count + 1)
    print(result)
