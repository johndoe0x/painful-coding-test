"""
PB0417 — for 누적 합계 목록

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 숫자를 더할 때마다 현재 누적 합계를 결과에 담는다.

연습 초점
---------
for 반복 중 상태 누적

구현할 함수
-----------
def running_sums_for(numbers: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- running_sums_for([2, 3, -1]) == [2, 5, 4]
- running_sums_for([]) == []
- running_sums_for([0]) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0417 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def running_sums_for(numbers: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0417")


def self_test() -> None:
    assert running_sums_for([2, 3, -1]) == [2, 5, 4]
    assert running_sums_for([]) == []
    assert running_sums_for([0]) == [0]
