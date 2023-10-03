import sys

input = sys.stdin.readline


def bt(n: int):
    # 종료 조건
    if n == N:
        print(*arr)
        return

    # 중복 허용 선택
    for i in range(1, M + 1):
        arr[n] = i
        bt(n + 1)


if __name__ == "__main__":
    M, N = map(int, input().split())
    arr = [-1] * N
    bt(0)
