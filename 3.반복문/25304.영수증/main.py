import sys

input = sys.stdin.readline

X = int(input())
N = int(input())

total = 0
for _ in range(N):
    price, n = map(int, input().split())
    total += price * n

print("Yes" if total == X else "No")
