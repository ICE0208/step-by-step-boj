import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        S = input().rstrip()
        print(S[0], S[-1], sep="")
