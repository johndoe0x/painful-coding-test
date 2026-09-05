"""
PB0203 — 유효한 직사각형

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
width와 height가 모두 0보다 크면 True를 반환하세요.

연습 초점
---------
두 수치 유효성의 AND

구현할 함수
-----------
def is_valid_rectangle(width: float, height: float) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- is_valid_rectangle(3, 4) is True
- is_valid_rectangle(0, 4) is False
- is_valid_rectangle(-1, -1) is False and is_valid_rectangle(3, 0) is False and is_valid_rectangle(3, -1) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0203 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_valid_rectangle(width: float, height: float) -> bool:
    raise NotImplementedError("TODO: PB0203")


def self_test() -> None:
    assert is_valid_rectangle(3, 4) is True
    assert is_valid_rectangle(0, 4) is False
    assert is_valid_rectangle(-1, -1) is False and is_valid_rectangle(3, 0) is False and is_valid_rectangle(3, -1) is False
