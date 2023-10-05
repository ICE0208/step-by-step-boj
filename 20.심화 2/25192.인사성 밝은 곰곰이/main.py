import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    s = set()
    result = 0

    for _ in range(N):
        cur = input().strip()
        if cur == "ENTER":
            result += len(s)
            s.clear()
            continue

        s.add(cur)

    result += len(s)
    print(result)
