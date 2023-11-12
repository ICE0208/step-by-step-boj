import sys

input = sys.stdin.readline

if __name__ == "__main__":
    lst = []
    for i in range(9):
        lst.append(int(input()))

    max_num = max(lst)
    max_order = lst.index(max_num) + 1
    print(max_num, max_order, sep="\n")
