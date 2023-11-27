import sys

input = sys.stdin.readline


def isallsame(arr, size, xstart, ystart):
    prev = arr[xstart][ystart]
    for i in range(xstart, xstart + size):
        for j in range(ystart, ystart + size):
            if arr[i][j] != prev:
                return False
            prev = arr[i][j]
    return True


def solution(arr, size, xstart, ystart):
    if size == 1 or isallsame(arr, size, xstart, ystart):
        count[arr[xstart][ystart]] += 1
        return

    subsize = size // 3
    for i in range(3):
        for j in range(3):
            solution(arr, subsize, xstart + subsize * i, ystart + subsize * j)


if __name__ == "__main__":
    count = [0, 0, 0]  #  0, 1, -1
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    solution(graph, N, 0, 0)

    print(count[2])
    print(count[0])
    print(count[1])
