import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    list = list(map(int, input().split()))

    cur_sum = 0
    max_sum = 0
    for i in range(N - K + 1):
        if i == 0:
            max_sum = cur_sum = sum(list[i : i + K])
        else:
            cur_sum -= list[i - 1]
            cur_sum += list[i + K - 1]

        max_sum = max(max_sum, cur_sum)

    print(max_sum)
