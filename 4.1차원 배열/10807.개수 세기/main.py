import sys

input = sys.stdin.readline

if __name__ == "__main__":
    input()
    lst = list(map(int, input().split(" ")))
    target = int(input())
    print(lst.count(target))
