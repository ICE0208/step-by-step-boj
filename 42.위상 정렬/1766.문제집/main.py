import sys
from queue import PriorityQueue

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    indegree = [0 for _ in range(N + 1)]
    next = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        indegree[b] += 1
        next[a].append(b)

    pq = PriorityQueue(maxsize=N)
    for i in range(1, N + 1):
        if indegree[i] == 0:
            pq.put(i)

    while pq.empty() == False:
        cur = pq.get()
        print(cur, end=" ")

        for n in next[cur]:
            indegree[n] -= 1
            if indegree[n] == 0:
                pq.put(n)
