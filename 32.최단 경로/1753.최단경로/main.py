import sys
import heapq

input = sys.stdin.readline
INF = 20000 * 10

if __name__ == "__main__":
    # 정점 개수, 간선 개수 입력 받기
    V, E = map(int, input().split())
    # 시작점 입력 받기
    start = int(input())
    # 각 노드에 연결된 노드와 경로 입력받기
    graph = [[] for _ in range(V + 1)]  # 1 ~ V
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    # 시작점에서 준비
    heap = []
    distance = [INF] * (V + 1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    # 연산 시작
    while heap:
        # 현재 노드까지의 거리, 현재 노드
        cur_dist, cur_node = heapq.heappop(heap)
        # 현재 노드가 이미 처리된 적이 있을 때 continue
        if cur_dist > distance[cur_node]:
            continue

        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for next_node, need_dist in graph[cur_node]:
            # 다음 노드까지의 거리
            cost = cur_dist + need_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    for i in range(1, V + 1):
        print("INF" if distance[i] == INF else distance[i])
