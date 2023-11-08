import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    mx = -1000000
    mn = 1000000
    for n in map(int, input().split()):
        mx = max(mx, n)
        mn = min(mn, n)
    print(mn, mx)
