# coding-test

취업 코딩 테스트 대비 문제 풀이 기록

---

## 목표

| 단계 | 내용 |
| --- | --- |
| 1차 | 프로그래머스 **Lv.1 완전 정복** |
| 2차 | **Lv.2 빈출 유형** (해시 · 정렬 · 완전탐색 · BFS/DFS) 안정 통과 |

---

## 문제 인덱스

<details open>
<summary><b>해시</b> — 카운팅, 딕셔너리 활용 <b>(6)</b></summary>

| 문제 | Lv | 풀이 | 핵심 / 막힌 지점 |
| --- | --- | --- | --- |
| [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | 1 | [코드](Python3/프로그래머스/1/42576. 완주하지 못한 선수/완주하지 못한 선수.py) | `list.remove()`가 O(n) → 루프 안에서 O(n²) 타임아웃. `Counter` 뺄셈으로 O(n) |
| [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845) | 1 | [코드](Python3/프로그래머스/1/1845. 폰켓몬/폰켓몬.py) | 실제 선택 x → min(종류 수, 뽑는 수) 두 상한 중 작은 값 |
| [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644) | 1 | [코드](Python3/프로그래머스/1/68644. 두 개 뽑아서 더하기/두 개 뽑아서 더하기.py) | 중복제거 set, 정렬 list.sort() 사용 |
| [최빈값 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/120812) | 0 | [코드](Python3/프로그래머스/0/120812. 최빈값 구하기/최빈값 구하기.py) | Counter객체 - most_common(): 많은 것부터 내림 차순 |
| [없는 숫자 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/86051) | 1 | [코드](Python3/프로그래머스/1/86051. 없는 숫자 더하기/없는 숫자 더하기.py) | |
| [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578) | **2** | [코드](Python3/프로그래머스/2/42578. 의상/의상.py) | dict.items(), Counter 사용 가능 |

</details>

<details>
<summary><b>구현 · 문자열</b> — 시뮬레이션, 문자열 처리 <b>(1)</b></summary>

| 문제 | Lv | 풀이 | 핵심 / 막힌 지점 |
| --- | --- | --- | --- |
| [자연수 뒤집어 배열로 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12932) | 1 | [코드](Python3/프로그래머스/1/12932. 자연수 뒤집어 배열로 만들기/자연수 뒤집어 배열로 만들기.py) | **map, reversed(str)** 사용 가능|

</details>

<details>
<summary><b>정렬 · 그리디</b> — 정렬 기준 설계, 탐욕법 <b>(0)</b></summary>

| 문제 | Lv | 풀이 | 핵심 / 막힌 지점 |
| --- | --- | --- | --- |
| | | | |

</details>

<details>
<summary><b>완전탐색</b> — 브루트포스, 순열 · 조합 <b>(0)</b></summary>

| 문제 | Lv | 풀이 | 핵심 / 막힌 지점 |
| --- | --- | --- | --- |
| | | | |

</details>

<details>
<summary><b>BFS · DFS</b> — 그래프 탐색 <b>(0)</b></summary>

| 문제 | Lv | 풀이 | 핵심 / 막힌 지점 |
| --- | --- | --- | --- |
| | | | |

</details>

---

## 문서

| 파일 | 내용 |
| --- | --- |
| [PLAN.md](PLAN.md) | 학습 계획 · 주차별 문제 목록 |
| [PATTERNS.md](PATTERNS.md) | 자주 쓰는 파이썬 패턴 |

---

## 진행 현황

| 시점 | 목표 | 누적 | 달성 |
| --- | --- | --- | --- |
| 08-02 | dict/set 조작 막힘 없음 | 20문제 | |
| 08-19 | 해시 · 정렬 · 완전탐색 Lv.2 통과 | 40문제 | |
| 09-06 | BFS 템플릿 백지 재현 성공 | 55문제 | |
| 09-중순 | 2문제 세트 시간 내 통과 | 60문제+ | |
