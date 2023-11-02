import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M, R = map(int, input().split())

    # 그래프 정보
    graph = [list() for _ in range(N + 1)]

    # 간선 연결 정보
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # DFS ---------
    stack = list()
    isVisit = [0 for _ in range(N + 1)]

    # 시작점 설정
    stack.append(R)

    # DFS 시작
    cnt = 1
    while stack:
        cur = stack.pop()
        if isVisit[cur] != 0:
            continue
        isVisit[cur] = cnt
        cnt += 1

        for next in sorted(graph[cur]):
            if isVisit[next] != 0:
                continue
            stack.append(next)

    # 출력
    print("\n".join(map(str, isVisit[1:])))
