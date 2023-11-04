import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    graph = [[] for _ in range(N + 1)]
    inCnt = [0 for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split(" "))
        graph[A].append(B)
        inCnt[B] += 1

    lst = []
    for i in range(1, N + 1):
        if inCnt[i] == 0:
            lst.append(i)

    while lst:
        cur = lst.pop()
        print(cur, end=" ")
        for next in graph[cur]:
            inCnt[next] -= 1
            if inCnt[next] == 0:
                lst.append(next)
