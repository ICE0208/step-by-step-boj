import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (N + 1)

    stack = list()
    stack.append(R)

    cnt = 1
    while stack:
        cur = stack.pop()
        if visited[cur] > 0:
            continue

        visited[cur] = cnt
        cnt += 1

        for next in sorted(graph[cur], reverse=True):
            if visited[next] > 0:
                continue

            stack.append(next)

    print("\n".join(map(str, visited[1:])))
