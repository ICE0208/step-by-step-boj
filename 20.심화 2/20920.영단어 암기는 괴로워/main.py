import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    words: dict[str, int] = dict()

    for _ in range(N):
        word = input().rstrip()
        if len(word) < M:
            continue
        words[word] = words.get(word, 0) + 1

    arr = [(-value, -len(key), key) for key, value in words.items()]
    arr.sort()
    for _, _, word in arr:
        print(word)
