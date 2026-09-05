"""
PB0101 — 세 값 왼쪽 회전

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
다중 할당 한 번으로 a, b, c를 왼쪽 회전해 반환하세요.

연습 초점
---------
tuple 패킹과 다중 할당

구현할 함수
-----------
def rotate_three(a: object, b: object, c: object) -> tuple[object, object, object]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- rotate_three(1, 2, 3) == (2, 3, 1)
- rotate_three('', None, False) == (None, False, '')
- rotate_three('x', 'x', 'x') == ('x', 'x', 'x')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0101 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rotate_three(a: object, b: object, c: object) -> tuple[object, object, object]:
    raise NotImplementedError("TODO: PB0101")


def self_test() -> None:
    assert rotate_three(1, 2, 3) == (2, 3, 1)
    assert rotate_three('', None, False) == (None, False, '')
    assert rotate_three('x', 'x', 'x') == ('x', 'x', 'x')
