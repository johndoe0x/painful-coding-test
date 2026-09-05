"""
PB0437 — 구간 안 배수

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 base에 대해 first 이상인 첫 배수부터 stop 이하까지 step=base인 range로 반환한다.

연습 초점
---------
계산한 시작값과 배수 step 결합

구현할 함수
-----------
def multiples_between_with_step(first: int, stop: int, base: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- multiples_between_with_step(5, 14, 3) == [6, 9, 12]
- multiples_between_with_step(7, 7, 7) == [7]
- multiples_between_with_step(8, 6, 2) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0437 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def multiples_between_with_step(first: int, stop: int, base: int) -> list[int]:
    raise NotImplementedError("TODO: PB0437")


def self_test() -> None:
    assert multiples_between_with_step(5, 14, 3) == [6, 9, 12]
    assert multiples_between_with_step(7, 7, 7) == [7]
    assert multiples_between_with_step(8, 6, 2) == []
