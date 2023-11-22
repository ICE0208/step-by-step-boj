import sys

input = sys.stdin.readline


def dfs(weight_lst, sum_lst, index, cur_sum):
    if index == len(weight_lst):
        sum_lst.append(cur_sum)
        return

    dfs(weight_lst, sum_lst, index + 1, cur_sum)

    if cur_sum + weight_lst[index] <= C:
        dfs(weight_lst, sum_lst, index + 1, cur_sum + weight_lst[index])


def binary_search(lst, target, start, end):
    while start <= end:
        mid = (end - start) // 2 + start
        if lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return end


if __name__ == "__main__":
    N, C = map(int, input().split())
    lst = list(map(int, input().split()))

    lst_a = lst[: N // 2]
    lst_b = lst[N // 2 :]

    sum_a = []
    sum_b = []
    dfs(lst_a, sum_a, 0, 0)
    dfs(lst_b, sum_b, 0, 0)

    sum_b.sort()
    result = 0
    for sub_sum_a in sum_a:
        target = C - sub_sum_a
        # target 최고 index 찾기
        index = binary_search(sum_b, target, 0, len(sum_b) - 1)
        result += index + 1

    print(result)
