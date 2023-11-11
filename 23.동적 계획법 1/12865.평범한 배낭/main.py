import sys

input = sys.stdin.readline

hashmap = dict()


def fn(i, rest_k):
    if i == 1:
        if rest_k < w[i]:
            return 0
        else:
            return v[i]

    if (i, rest_k) in hashmap:
        return hashmap[(i, rest_k)]

    if rest_k < w[i]:
        hashmap[(i, rest_k)] = fn(i - 1, rest_k)
    else:
        hashmap[(i, rest_k)] = max(fn(i - 1, rest_k), fn(i - 1, rest_k - w[i]) + v[i])

    return hashmap[(i, rest_k)]


if __name__ == "__main__":
    N, K = map(int, input().split())
    w = [0] + [0 for _ in range(N)]
    v = [0] + [0 for _ in range(N)]

    for i in range(1, N + 1):
        w[i], v[i] = map(int, input().split())

    print(fn(N, K))
