import sys

input = sys.stdin.readline

if __name__ == "__main__":
    # 입력 받기
    n = int(input())
    nums_set = set(map(int, input().split()))
    x = int(input())

    cnt = 0
    for num in nums_set:
        if x - num in nums_set:
            cnt += 1

    result = cnt // 2
    print(result)
