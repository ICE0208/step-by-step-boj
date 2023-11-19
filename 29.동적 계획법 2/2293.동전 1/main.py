import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    lst = [0 for i in range(k + 1)]

    coins = [0]
    for _ in range(n):
        coins.append(int(input()))

    for coin_i in range(1, n + 1):
        for target_v in range(1, k + 1):
            a = lst[target_v]
            b = (
                lst[target_v - coins[coin_i]]
                if target_v - coins[coin_i] > 0
                else 1
                if target_v == coins[coin_i]
                else 0
            )

            lst[target_v] = a + b

    print(lst[k])
