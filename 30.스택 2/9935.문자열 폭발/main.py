import sys

input = sys.stdin.readline

if __name__ == "__main__":
    S = input().rstrip()
    target = list(input().rstrip())
    lst = []

    for c in S:
        lst.append(c)
        while lst[-len(target) :] == target:
            del lst[-len(target) :]

    print("".join(lst) if lst else "FRULA")
