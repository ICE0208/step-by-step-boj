import sys

input = sys.stdin.readline

if __name__ == "__main__":
    S = input().rstrip()
    q = int(input())

    m = [[0 for j in range(26)] for i in range(len(S))]

    m[0][ord(S[0]) - 97] = 1
    for i in range(1, len(S)):
        # [1] 수정한 부분
        # for j in range(26):
        #     m[i][j] = m[i - 1][j]
        m[i] = m[i - 1][:]

        # [2] 수정한 부분
        # m[i][ord(S[i]) - ord("a")] = m[i - 1][ord(S[i]) - ord("a")] + 1
        m[i][ord(S[i]) - ord("a")] += 1

    for _ in range(q):
        target, l, r = input().split()
        l, r = map(int, [l, r])

        if l > 0:
            print(m[r][ord(target) - ord("a")] - m[l - 1][ord(target) - ord("a")])
        else:
            print(m[r][ord(target) - ord("a")])
