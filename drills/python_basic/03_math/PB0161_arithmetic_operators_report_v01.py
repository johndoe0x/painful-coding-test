"""
PB0161 — 기본 산술 연산표

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
b가 0이 아닐 때 +, -, *, //, % 결과를 지정된 키로 반환하세요.

연습 초점
---------
기본 산술 연산자의 결과 차이

구현할 함수
-----------
def arithmetic_report(a: int, b: int) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- arithmetic_report(7, 3) == {'add': 10, 'sub': 4, 'mul': 21, 'floordiv': 2, 'mod': 1}
- arithmetic_report(0, 2) == {'add': 2, 'sub': -2, 'mul': 0, 'floordiv': 0, 'mod': 0}
- arithmetic_report(-7, 3) == {'add': -4, 'sub': -10, 'mul': -21, 'floordiv': -3, 'mod': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0161 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def arithmetic_report(a: int, b: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0161")


def self_test() -> None:
    assert arithmetic_report(7, 3) == {'add': 10, 'sub': 4, 'mul': 21, 'floordiv': 2, 'mod': 1}
    assert arithmetic_report(0, 2) == {'add': 2, 'sub': -2, 'mul': 0, 'floordiv': 0, 'mod': 0}
    assert arithmetic_report(-7, 3) == {'add': -4, 'sub': -10, 'mul': -21, 'floordiv': -3, 'mod': 2}
