# 9184.신나는 함수 실행

## 문제 링크

(https://www.acmicpc.net/problem/9184)

## 접근 방법

```
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
```

**_(문제에 나와있는 의사 코드)_**

문제에 나와있는 의사 코드를 보고 그대로 코드를 작성한 뒤, `메모이제이션`만 추가하면 된다. 파이썬을 기준으로 딕셔너리와 튜플을 이용하여 쉽게 해결할 수 있었다.

자바로 문제를 풀 때는 3차원 배열을 이용하여 풀었다.

## 참고 자료

NULL
