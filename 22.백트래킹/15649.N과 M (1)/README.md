# 15649.N과 M (1)

## 문제 링크

(https://www.acmicpc.net/problem/15649)

## 접근 방법

재귀 함수를 이용하여 중복없이 M개의 수를 선택하여 출력한다. (오름차순)

### 재귀 함수 들어가기 전

```python
visited = [False] * (N + 1)
```

중복을 피하기 위해 visited 배열을 만들어서 이용하였다.

### 재귀 함수 내부

```python
def backtrack(n, lst):
    # 나머지 코드
```

n은 현재 선택된 수의 개수, lst는 현재 선택된 수가 순서대로 담겨진 리스트이다.

```python
if n == M:
    print(*lst)
    return
```

현재 선택된 수의 개수가 M개 라면, 리스트에 담겨진 수를 출력한다.

```python
for i in range(1, N + 1):
    if visited[i] == True:
        continue

    visited[i] = True
    backtrack(n + 1, lst + [i])
    visited[i] = False
```

수를 더 선택해야 할 상황이라면, 1부터 N까지 수를 차례대로 선택한다.

이때, visited 배열을 이용하여 이미 선택된 수 라면 continue를 통해 다음 수로 넘어가고, 아직 선택되지 않은 수 라면, visited[선택된 수]를 True로 변경하고 재귀 호출을 한다.

재귀 호출을 할 때 n(현재 선택된 수의 개수)을 1 증가시키고 lst에 현재 선택된 수를 추가하여 넘겨준다.

재귀 호출이 끝났을 때 visited[선택된 수]를 다시 False로 되돌린다.

### 전체 코드

```python
import sys

input = sys.stdin.readline


def backtrack(n, lst):
    if n == M:
        print(*lst)
        return

    for i in range(1, N + 1):
        if visited[i] == True:
            continue

        visited[i] = True
        backtrack(n + 1, lst + [i])
        visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [False] * (N + 1)

    backtrack(0, [])

```

## 참고 자료

- (https://youtu.be/exwk905In0U?si=q3dnMgxWcF2H9d3W)
