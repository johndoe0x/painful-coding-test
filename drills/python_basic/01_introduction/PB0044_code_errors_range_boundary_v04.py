"""
PB0044 — range 끝값 누락 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 range(start, end)를 사용해 end를 제외합니다. start부터 end까지 양끝을 포함하고 start > end이면 빈 리스트를 반환하도록 고치세요.

연습 초점
---------
range의 배타적 stop과 포함 경계의 변환

구현할 함수
-----------
def inclusive_numbers(start: int, end: int) -> list[int]:

예시 및 필수 테스트
-------------------
- inclusive_numbers(2, 4) == [2, 3, 4]
- inclusive_numbers(5, 4) == []
- inclusive_numbers(0, 0) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0044 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def inclusive_numbers(start: int, end: int) -> list[int]:
    return list(range(start, end))


def self_test() -> None:
    assert inclusive_numbers(2, 4) == [2, 3, 4]
    assert inclusive_numbers(5, 4) == []
    assert inclusive_numbers(0, 0) == [0]
