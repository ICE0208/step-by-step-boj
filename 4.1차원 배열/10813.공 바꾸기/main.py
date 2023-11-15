import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    basket = [i for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        basket[a], basket[b] = basket[b], basket[a]

    for i in range(1, N + 1):
        print(basket[i], end=" ")
