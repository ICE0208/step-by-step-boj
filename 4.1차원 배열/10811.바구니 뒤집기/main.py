import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    basket = [i for i in range(0, N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())

        basket[a : b + 1] = basket[b : a - 1 : -1]

    for i in range(1, N + 1):
        print(basket[i], end=" ")
