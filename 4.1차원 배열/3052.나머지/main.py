import sys

input = sys.stdin.readline

FORTY_TWO = 42

if __name__ == "__main__":
    s = set()

    for _ in range(10):
        num = int(input())
        s.add(num % 42)

    print(len(s))
