import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    start, dest = map(int, input().split())

    lst = [100000 for _ in range(100001)]
    q = deque()
    q.append((start, 0))  # pos, cost

    while q:
        cur_pos, cur_cost = q.popleft()

        if cur_cost >= lst[cur_pos]:
            continue
        lst[cur_pos] = cur_cost

        if cur_pos > 0:
            next_pos, next_cost = cur_pos - 1, cur_cost + 1
            if lst[next_pos] > next_cost:
                q.append((next_pos, next_cost))

        if cur_pos < 100000:
            next_pos, next_cost = cur_pos + 1, cur_cost + 1
            if lst[next_pos] > next_cost:
                q.append((next_pos, next_cost))

        if 0 < cur_pos <= 50000:
            next_pos, next_cost = cur_pos * 2, cur_cost
            if lst[next_pos] > next_cost:
                q.append((next_pos, next_cost))

    print(lst[dest])
