# 2156.포도주 시식

## 문제 링크

(https://www.acmicpc.net/problem/2156)

## 접근 방법

wine 배열에 각 포도주의 양을 저장하고, dp 배열에 i번째 잔까지 탐색했을 때 최대로 마실 수 있는 포도주의 양을 저장한다.

dp[i]를 계산할 때는 아래 세 조건을 확인해야 한다.

1. i번째 잔을 마시지 않을 때
2. i-1번째 잔을 마신 상태에서 i번째 잔을 마실 때
3. i-1번째 잔을 마시지 않은 상태에서 i번째 잔을 마실 때

i>3 일 때, 각 조건일 때의 값은 아래와 같이 계산한다.

1. dp[i-1]
2. dp[i-3] + wine[i-1] + wine[i]
3. dp[i-2] + wine[i]

dp[i]는 계산한 1, 2, 3번 중 제일 큰 값이 된다.

이를 파이썬으로 나타내면 다음과 같이 된다.

```python
dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])
```

## 참고 자료

- (https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2156%EB%B2%88.-%ED%8F%AC%EB%8F%84%EC%A3%BC-%EC%8B%9C%EC%8B%9D)
- (https://st-lab.tistory.com/135) - Top-Down 문제 풀이
