"""
PB0103 — 몫과 나머지 풀기

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
divmod 결과를 quotient와 remainder에 한 번에 할당해 딕셔너리로 반환하세요. divisor는 0이 아닙니다.

연습 초점
---------
반환 tuple 언패킹

구현할 함수
-----------
def unpack_division(number: int, divisor: int) -> dict[str, int]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- unpack_division(17, 5) == {'quotient': 3, 'remainder': 2}
- unpack_division(0, 3) == {'quotient': 0, 'remainder': 0}
- unpack_division(5, 5) == {'quotient': 1, 'remainder': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0103 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unpack_division(number: int, divisor: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0103")


def self_test() -> None:
    assert unpack_division(17, 5) == {'quotient': 3, 'remainder': 2}
    assert unpack_division(0, 3) == {'quotient': 0, 'remainder': 0}
    assert unpack_division(5, 5) == {'quotient': 1, 'remainder': 0}
