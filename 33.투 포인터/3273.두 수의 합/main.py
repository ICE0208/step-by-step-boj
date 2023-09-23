import sys

input = sys.stdin.readline


if __name__ == "__main__":
    # 입력 받기
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    # 투 포인터를 위해 정렬을 수행
    nums.sort()

    # left, right 포인터를 양 끝으로 지정
    left, right = 0, n - 1
    # 경우의 수를 저장할 cnt 변수
    cnt = 0

    # 투 포인터 탐색 시작
    while left < right:
        cur = nums[left] + nums[right]
        # 같을 때 left, right를 모두 이동
        # (서로 다른 수열이므로)
        if cur == x:
            cnt += 1
            left, right = left + 1, right - 1
        # 클 때 더 작아져야 하므로 right를 이동
        elif cur > x:
            right -= 1
        # 작을 때 더 커져야 하므로 left를 이동
        else:
            left += 1

    # 출력
    print(cnt)
