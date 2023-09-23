# 3273.두 수의 합

## 문제 링크

(https://www.acmicpc.net/problem/3273)

## 접근 방법

투 포인터를 이용하여 풀면 쉽게 해결할 수 있다.

1. 오름차순 정렬을 한다.
   ```python
   nums.sort()
   ```
2. 양 끝에서 시작하는 투 포인터로 시작한다.
   ```python
   left, right = 0, n - 1
   ```
3. 조건에 따라 left, right 포인터를 움직이면서 합이 x를 만족하는 경우의 수를 센다.
   ```python
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
   ```

## 참고 자료

NULL
