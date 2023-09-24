# 12789.도키도키 간식드리미

## 문제 링크

(https://www.acmicpc.net/problem/12789)

## 접근 방법

_**현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다.**_

위 문장에서 `반대는 불가능하다`라는 조건 덕분에 스택과 큐를 이용하면 쉽게 구현할 수 있다. 사실 `현재 줄 서있는 곳`을 reverse 하면 스택만으로도 구현할 수 있다.

큐를 `현재 줄 서있는 공간`이라고 하고 스택을 `한 명씩만 설 수 있는 공간`이라고 했을 때 로직은 다음과 같다.

- 큐의 첫 번째 원소가 현재 번호표 순서와 같으면 큐를 pop한다.
- 스택이 비지 않았을 때 스택의 첫 번째 원소가 현재 번호표 순서와 같으면 스택을 pop한다.
- 큐와 스택의 첫 번째 원소가 모두 현재 번호표 순서가 아니면 큐를 pop하고 pop된 원소를 스택에 push한다.
- 큐가 빌 때 까지 위 과정을 반복한다.
- 큐가 비었다면 스택에서 원소를 하나씩 pop하면서 번호표 순서와 맞는지 확인한다. 만약 큐가 비었을 때 스택도 비어있는 상태라면 Nice를 출력한다.
- 스택이 번호표 순서대로 되어있다면 Nice를 출력하고 아니라면 Sad를 출력한다.

(큐와 스택의 첫 번째 원소는 각각 pop했을 때 나올 원소이다.)

위 로직을 파이썬 코드로 구현하면 아래와 같다.

```python
while Q:
    cur = Q[0]
    if cur == target:
        Q.popleft()
        target += 1
        continue
    elif S and S[-1] == target:
        S.pop()
        target += 1
        continue
    else:
        S.append(Q.popleft())

while S:
    cur = S[-1]
    if cur != target:
        break
    S.pop()
    target += 1

print("Sad" if S else "Nice")
```

## 참고 자료

NULL
