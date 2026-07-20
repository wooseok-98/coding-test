# 자주 쓰는 파이썬 패턴

검색 없이 손이 먼저 나갈 때까지 **매일 5분 백지 타이핑**

---

## 매일 타이핑할 6줄

```python
d[k] = d.get(k, 0) + 1                    # 카운팅
best = max(d.values())                    # 최댓값
[k for k in d if d[k] == best]            # 조건 필터링
sorted(lst, key=lambda x: (-x[1], x[0]))  # 다중 기준 정렬
from collections import Counter, deque
dq = deque(); dq.popleft()                # 큐 (BFS용)
```

---

## 딕셔너리

```python
d = {}
d[k] = d.get(k, 0) + 1        # 없으면 0에서 시작해 +1
d.keys(), d.values(), d.items()
for k, v in d.items(): ...

from collections import Counter
Counter(lst)                  # 리스트 통째로 카운팅
Counter(lst).most_common(1)   # [(최빈값, 개수)]
```

> `.get()`은 **읽기 전용** — 값을 넣으려면 반드시 `d[k] = ...`

## 집합

```python
set(lst)                      # 중복 제거
set_a - set_b                 # 차집합
set_a & set_b                 # 교집합
```

## 정렬

```python
sorted(lst)                          # 원본 유지, 새 리스트 반환
lst.sort()                           # 원본 변경, 반환값 None
sorted(lst, reverse=True)
sorted(lst, key=lambda x: -x[1])     # 내림차순은 부호 반전
sorted(lst, key=lambda x: (-x[1], x[0]))  # 1순위 개수↓, 2순위 이름↑
```

> 튜플 정렬은 **앞 원소부터** 비교, 같을 때만 뒤 원소 확인

## 문자열

```python
s.strip()                     # 양끝 공백·개행 제거
s.split()                     # 공백 기준 분리
''.join(lst)                  # 리스트 → 문자열
s.replace('a', 'b')
s.isdigit(), s.isalpha()
s.lower(), s.upper()
ord('a'), chr(97)             # 문자 ↔ 아스키
```

## 입출력 (구름 · 표준입출력)

```python
import sys
input = sys.stdin.readline

n = int(input())                          # 숫자 하나
a, b = map(int, input().split())          # 여러 개
arr = list(map(int, input().split()))     # 리스트
s = input().strip()                       # 문자열은 strip 필수

print(*arr)                               # 공백 구분 출력
print('\n'.join(map(str, arr)))           # 줄바꿈 출력
```

## BFS 템플릿

```python
from collections import deque

def bfs(start):
    q = deque([start])
    visited = {start}
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
```

**격자 탐색 방향 벡터**

```python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
if 0 <= nx < n and 0 <= ny < m:   # 경계 체크
```

---

## 시간복잡도 역산

문제를 읽으면 **N 범위부터 확인** 후 구현 시작

| N 범위 | 필요 복잡도 | 대표 기법 |
| --- | --- | --- |
| N ≤ 10 | `O(N!)`, `O(2^N)` | 완전탐색, 순열 |
| N ≤ 1,000 | `O(N^2)` | 이중 반복문 |
| N ≤ 100,000 | `O(N log N)` | 정렬, 힙, 이분탐색 |
| N ≤ 1,000,000 | `O(N)` | 투포인터, 누적합 |
