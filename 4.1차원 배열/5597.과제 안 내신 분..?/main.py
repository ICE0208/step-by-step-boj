import sys

input = sys.stdin.readline

if __name__ == "__main__":
    lst = [0 for i in range(31)]
    for _ in range(28):
        a = int(input())
        lst[a] = 1

    for i in range(1, 31):
        if lst[i] == 0:
            print(i)
