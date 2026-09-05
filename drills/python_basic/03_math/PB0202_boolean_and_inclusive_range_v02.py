"""
PB0202 — 범위 안의 값

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
value가 minimum 이상이고 maximum 이하이면 True를 반환하세요.

연습 초점
---------
두 경계 조건의 AND

구현할 함수
-----------
def is_within_range(value: int, minimum: int, maximum: int) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- is_within_range(5, 1, 10) is True
- is_within_range(1, 1, 10) is True and is_within_range(10, 1, 10) is True
- is_within_range(11, 1, 10) is False and is_within_range(0, 1, 10) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0202 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_within_range(value: int, minimum: int, maximum: int) -> bool:
    raise NotImplementedError("TODO: PB0202")


def self_test() -> None:
    assert is_within_range(5, 1, 10) is True
    assert is_within_range(1, 1, 10) is True and is_within_range(10, 1, 10) is True
    assert is_within_range(11, 1, 10) is False and is_within_range(0, 1, 10) is False
