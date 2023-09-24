import sys
from collections import deque

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    Q = deque(map(int, input().split()))
    S = list()  # stack

    target = 1
    while Q:
        cur = Q[0]
        if cur == target:
            Q.popleft()
            target += 1
            continue
        elif S and S[-1] == target:
            S.pop()
            target += 1
            continue
        else:
            S.append(Q.popleft())

    while S:
        cur = S[-1]
        if cur != target:
            break
        S.pop()
        target += 1

    print("Sad" if S else "Nice")
