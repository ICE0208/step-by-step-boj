import sys


def removeCenter(start, end):
    global last
    length = end - start + 1
    if length == 1:
        print(" " * (start - last - 1), end="")
        print("-" * (end - start + 1), end="")
        last = end
        return

    cutLength = length // 3
    cl = start + cutLength
    cr = end - cutLength
    removeCenter(start, cl - 1)
    removeCenter(cr + 1, end)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for line in lines:
        N = int(line)
        k = 3**N
        last = 0

        removeCenter(1, k)
        print()
