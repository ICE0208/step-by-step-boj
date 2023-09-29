# 1912.연속합

## 문제 링크

(https://www.acmicpc.net/problem/1912)

## 접근 방법

### 브루트 포스

브루트 포스 방식(이중 for문)으로 전체 탐색하면 이론상 풀 수 있다.
다만, 이중 for문으로 풀면 시간 복잡도가 O(n^2)이 되어 시간 초과가 발생한다.

### 동적 계획법

동적 계획법을 이용하면 O(n)의 시간 복잡도로 이 문제를 해결할 수 있다.

`동적 계획법: 직전에 계산한 결과값을 기억해두고 이를 활용하여 문제를 푸는 것.`

이 문제에서 점화식을 만들어 보면 아래와 같다.

`(n번까지의 연속합 중 최댓값) = max(n-1번까지의 연속합 중 최대값 + n번 값, n번 값)`

이 점화식을 이용하여 문제를 해결해보자

- Top Down 방식 (재귀)

재귀 함수으로 구현하면 다음과 같다.

```python
dp[0] = nums[0]
def recur(k):
    if dp[k] != None:
        return dp[k]

    dp[k] = max(recur(k - 1) + arr[k], arr[k])
    return dp[k]
```

다만, 이렇게 하면 재귀 깊이가 너무 깊어져서 에러가 발생할 수 있다.
[(참고)](https://help.acmicpc.net/judge/rte/RecursionError)

파이썬 기준으로 `sys.setrecursionlimit()`을 사용하여 해결을 하였지만 만약 입력값 n의 범위가 더 커진다면 문제를 해결하는데 한계가 있으므로 반복문을 활용하여 풀어보자.

- Bottom Up 방식 (반복문)

```python
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])
```

dp[n]의 값은 `n번째 수를 마지막으로 하는 연속합 중 최댓값`이다. 그러므로 구한 dp 배열의 원소들 중 최댓값이 이 문제의 정답이 된다.

## 참고 자료

- (https://st-lab.tistory.com/140)
- (https://rightbellboy.tistory.com/83)
- (https://folivora.tistory.com/89)
