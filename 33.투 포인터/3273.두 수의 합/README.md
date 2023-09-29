# 3273.두 수의 합

## 문제 링크

(https://www.acmicpc.net/problem/3273)

## 접근 방법

### 투 포인터를 이용한 방법 (main.py, Main.java)

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

### Set을 이용한 방법 [main2.py]

Set을 이용하면 이 문제를 간단히 풀 수 있다. 문제 조건에 맞는 쌍 중 하나를 `(a, b)`라고 할 때 `a + b = x` 이므로, `a`가 주어졌을 때, `x - a` 가 존재한다면 `(a, b)` 쌍을 만들 수 있다는 뜻이 된다. 모든 원소를 탐색하면서 a가 주어졌을 때 x - a가 있는 경우의 수를 세주면 된다.

단, 이렇게만 하면 `(a, b)`와 `(b, a)`가 각각 다른 쌍으로 카운트 되는데 문제 조건에 `a < b`라고 나와있으므로 카운트 된 수를 2로 나눠줘야 정답이 된다.

## 참고 자료

- (https://code-lab1.tistory.com/94)
