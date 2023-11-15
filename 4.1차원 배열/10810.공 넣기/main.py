import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    basket = [0 for _ in range(N + 1)]

    for _ in range(M):
        i, j, k = map(int, input().split())
        for n in range(i, j + 1):
            basket[n] = k

    print(" ".join(map(str, basket[1:])))
