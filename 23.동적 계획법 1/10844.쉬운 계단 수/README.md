# 10844.쉬운 계단 수

## 문제 링크

(https://www.acmicpc.net/problem/10844)

## 접근 방법

점화식을 세우고 dp를 이용하여 해결한다.

### 점화식

dp[N][L] : 끝이 L이고 길이가 N인 계단의 수

- `L==0` 일 때, `dp[N][L] = dp[N-1][1]`
- `L==9` 일 때, `dp[N][L] = dp[N-1][8]`
- `1<=L<=8` 일 때, `dp[N][L] = p[N-1][L-1] + dp[N-1][L+1]`

(N==1이고 1<=L<=9 일 때, dp[N][L] = 0)

해당 점화식으로 푼 소스 코드는 `main.py`, `Main.java` 이다.

## 참고 자료

(https://ji-gwang.tistory.com/275)
(https://st-lab.tistory.com/134)
