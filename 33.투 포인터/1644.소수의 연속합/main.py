import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a = [True for _ in range(4000001)]

    for i in range(2, 4000001):
        if a[i] == False:
            continue
        for j in range(i + i, 4000001, i):
            a[j] = False

    primeList = []
    for i in range(2, 4000001):
        if a[i]:
            primeList.append(i)

    N = int(input())
    left, right = 0, 0

    cur = primeList[right]
    cnt = 0
    maxIndex = len(primeList) - 1
    while left <= right:
        if cur >= N:
            if cur == N:
                cnt += 1
            cur -= primeList[left]
            left += 1
        else:
            right += 1
            if right > maxIndex:
                break
            cur += primeList[right]

    print(cnt)
