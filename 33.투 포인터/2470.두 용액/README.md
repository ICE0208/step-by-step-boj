# 2470.두 용액

## 문제 링크

(https://www.acmicpc.net/problem/2470)

## 접근 방법

오름차순 후 양쪽 끝에서 좁혀오는 형태의 투 포인터를 이용하면 쉽게 해결할 수 있다.

1. 입력 받고 오름차순 후 투 포인터 준비

```python
N = int(input())
# 입력 받으면서 오름차순 정렬
list = sorted(list(map(int, input().split())))

# 포인터를 각각 양쪽 끝에 배치
left, right = 0, N - 1
# (특성값, 용액1, 용액2)
result = (float("inf"), 0, 0)
```

2. 탐색하면서 정답 찾기

```python
while left < right:
    cur = list[left] + list[right]

    # 특성값 업데이트
    if abs(cur) < abs(result[0]):
        result = (cur, list[left], list[right])

    # left or right 업데이트
    if cur > 0:
        right -= 1
    else:
        left += 1
```

이 때, 양수 음수 상관없이 0에 가장 가까운 값을 찾아야 하므로 절댓값을 이용한다.

3. 정답 출력

```python
print(result[1], result[2])
```

출력 조건에 오름차순으로 출력해야 한다고 나와있는데, 정렬된 상태에서 left는 항상 right의 왼쪽에 위치하므로 result[1]은 항상 result[2] 보다 작다.

## 참고 자료

NULL
