s = input()
lst = [-1 for _ in range(ord("a"), ord("z") + 1)]

for i, c in enumerate(s):
    index = ord(c) - ord("a")
    if lst[index] == -1:
        lst[index] = i

for l in lst:
    print(l, end=" ")
