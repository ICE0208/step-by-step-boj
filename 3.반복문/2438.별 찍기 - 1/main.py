import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print("*" * (i + 1))
