"""
PB0106 — 네 값 오른쪽 회전

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
다중 할당으로 마지막 값을 맨 앞으로 옮기고 나머지를 오른쪽으로 한 칸 이동하세요.

연습 초점
---------
여러 변수의 동시 갱신

구현할 함수
-----------
def rotate_four_right(a: object, b: object, c: object, d: object) -> tuple[object, object, object, object]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- rotate_four_right(1, 2, 3, 4) == (4, 1, 2, 3)
- rotate_four_right('', None, False, 0) == (0, '', None, False)
- rotate_four_right('x', 'x', 'x', 'x') == ('x', 'x', 'x', 'x')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0106 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rotate_four_right(a: object, b: object, c: object, d: object) -> tuple[object, object, object, object]:
    raise NotImplementedError("TODO: PB0106")


def self_test() -> None:
    assert rotate_four_right(1, 2, 3, 4) == (4, 1, 2, 3)
    assert rotate_four_right('', None, False, 0) == (0, '', None, False)
    assert rotate_four_right('x', 'x', 'x', 'x') == ('x', 'x', 'x', 'x')
