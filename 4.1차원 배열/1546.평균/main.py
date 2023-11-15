import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    max_score = max(lst)

    for i in range(N):
        lst[i] = lst[i] / max_score * 100

    print(sum(lst) / N)
