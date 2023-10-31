import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        for j in range(i, N - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()
