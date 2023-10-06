import sys

input = sys.stdin.readline

if __name__ == "__main__":
    dance = set()
    dance.add("ChongChong")

    N = int(input())

    for _ in range(N):
        a, b = input().split()
        if any(x in dance for x in (a, b)):
            dance.add(a)
            dance.add(b)

    print(len(dance))
