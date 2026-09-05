"""
PB0381 — while 카운트다운

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while을 사용해 start부터 1까지 감소하는 정수 리스트를 만들며 start가 1 미만이면 빈 리스트를 반환한다.

연습 초점
---------
조건이 거짓이 될 때까지 while 반복

구현할 함수
-----------
def countdown(start: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- countdown(3) == [3, 2, 1]
- countdown(0) == []
- countdown(1) == [1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0381 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def countdown(start: int) -> list[int]:
    raise NotImplementedError("TODO: PB0381")


def self_test() -> None:
    assert countdown(3) == [3, 2, 1]
    assert countdown(0) == []
    assert countdown(1) == [1]
