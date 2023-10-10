import sys

input = sys.stdin.readline


def calcAbility(member: set) -> int:
    result = 0
    memList = list(member)
    for i in range(0, len(member)):
        for j in range(i + 1, len(member)):
            a = memList[i]
            b = memList[j]
            result += arr[a][b] + arr[b][a]
    return result


def dfs(n: int, s: set, last: int):
    if N // 2 == n:
        # 능력치 차 계산하기
        global result
        result = min(result, abs(calcAbility(s) - calcAbility(all - s)))
        return

    for i in range(last + 1, N):
        if i in s:
            continue

        dfs(n + 1, s | {i}, i)


if __name__ == "__main__":
    result = float("inf")
    N = int(input())

    all = set([i for i in range(N)])
    arr = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    dfs(0, set([]), -1)

    print(result)
