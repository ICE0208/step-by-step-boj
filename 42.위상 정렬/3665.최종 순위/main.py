import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    for SUB_T in range(T):
        n = int(input())
        lst = [0] + list(map(int, input().split()))

        next_lst = [set() for _ in range(n + 1)]
        in_cnt = [0 for _ in range(n + 1)]
        before = set()
        for i in range(n, 0, -1):
            next_lst[lst[i]] = set(before)
            in_cnt[lst[i]] = i - 1
            before.add(lst[i])
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            if b in next_lst[a]:
                next_lst[a].remove(b)
                in_cnt[b] -= 1
                next_lst[b].add(a)
                in_cnt[a] += 1
            else:
                next_lst[b].remove(a)
                in_cnt[a] -= 1
                next_lst[a].add(b)
                in_cnt[b] += 1

        stack = list()
        for i in range(1, n + 1):
            if in_cnt[i] == 0:
                stack.append(i)

        result = []
        while stack:
            if len(stack) > 1:
                break
            cur = stack.pop()
            result.append(str(cur))

            for next in next_lst[cur]:
                in_cnt[next] -= 1
                if in_cnt[next] == 0:
                    stack.append(next)
        if stack or len(result) != n:
            print("IMPOSSIBLE")
        else:
            print(" ".join(result))
