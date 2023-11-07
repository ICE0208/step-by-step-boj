import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, X = map(int, input().split())
    A = map(int, input().split())
    for a in A:
        if a < X:
            print(a, end=" ")
