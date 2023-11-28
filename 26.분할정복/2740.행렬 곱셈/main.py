import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    M, K = map(int, input().split())
    B = []
    for _ in range(M):
        B.append(list(map(int, input().split())))

    result = [[0 for i in range(K)] for j in range(N)]

    for n in range(N):
        for k in range(K):
            for m in range(M):
                result[n][k] += A[n][m] * B[m][k]

    for result_line in result:
        print(" ".join(map(str, result_line)))
