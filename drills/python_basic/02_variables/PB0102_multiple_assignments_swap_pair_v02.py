"""
PB0102 — 두 값 교환

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
임시 변수 없이 다중 할당으로 두 값을 교환하세요.

연습 초점
---------
Python식 값 교환

구현할 함수
-----------
def swap_two(left: object, right: object) -> tuple[object, object]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- swap_two(1, 2) == (2, 1)
- swap_two('', None) == (None, '')
- swap_two('same', 'same') == ('same', 'same')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0102 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def swap_two(left: object, right: object) -> tuple[object, object]:
    raise NotImplementedError("TODO: PB0102")


def self_test() -> None:
    assert swap_two(1, 2) == (2, 1)
    assert swap_two('', None) == (None, '')
    assert swap_two('same', 'same') == ('same', 'same')
