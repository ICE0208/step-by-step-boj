import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    b = list(map(int, input().split()))

    a.sort()
    for c in b:
        pass

        start = 0
        end = len(a) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if a[mid] == c:
                break
            elif a[mid] < c:
                start = mid + 1
            else:
                end = mid - 1
        if start <= end:
            print(1)
        else:
            print(0)
