# 26069.붙임성 좋은 총총이

## 문제 링크

(https://www.acmicpc.net/problem/26069)

## 접근 방법

set을 이용하여 현재 무지개 댄스를 추고 있는 사람을 판별하면서 문제를 해결한다.

1. 처음에 ChongChong이 춤을 추고 있으므로 set에 추가시켜준다.
   ```python
   dance = set()
   dance.add("ChongChong")
   ```
2. 만난 사람 둘 중에 한 명이 set에 포함될 때, 두 명 모두 set에 추가시켜준다.
   ```python
   N = int(input())
   for _ in range(N):
       a, b = input().split()
       if any(x in dance for x in (a, b)):
           dance.add(a)
           dance.add(b)
   ```
3. set의 크기가 현재 춤을 추고 있는 사람의 수이다.
   ```python
   print(len(dance))
   ```

## 참고 자료

NULL
