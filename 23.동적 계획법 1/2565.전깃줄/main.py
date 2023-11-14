import sys

input = sys.stdin.readline


def lis(start):
    ret = cache[start]
    if ret != -1:
        return cache[start]

    ret = 1
    for next in range(start + 1, N):
        if seq[start] < seq[next]:
            ret = max(ret, lis(next) + 1)

    cache[start] = ret
    return ret


if __name__ == "__main__":
    N = int(input())
    cache = [-1 for _ in range(N)]

    lst = [-1 for _ in range(501)]
    for _ in range(N):
        a, b = map(int, input().split())
        lst[a] = b

    seq = list()
    for l in lst:
        if l == -1:
            continue
        seq.append(l)

    lis_result = 0
    for i in range(0, N):
        lis_result = max(lis_result, lis(i))
    result = N - lis_result
    print(result)
