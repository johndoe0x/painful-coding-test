"""
PB0432 — 구간 짝수 나열

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
start 이상 stop 미만의 첫 짝수를 찾아 step 2인 range로 짝수만 반환한다.

연습 초점
---------
시작값 정렬 후 고정 step 사용

구현할 함수
-----------
def even_numbers_in_range(start: int, stop: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- even_numbers_in_range(3, 10) == [4, 6, 8]
- even_numbers_in_range(2, 3) == [2]
- even_numbers_in_range(-3, 2) == [-2, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0432 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def even_numbers_in_range(start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0432")


def self_test() -> None:
    assert even_numbers_in_range(3, 10) == [4, 6, 8]
    assert even_numbers_in_range(2, 3) == [2]
    assert even_numbers_in_range(-3, 2) == [-2, 0]
