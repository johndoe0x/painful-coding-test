"""
PB0148 — 서로 다른 값을 문자열로 결합

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 값을 str로 변환한 뒤 separator로 연결하세요.

연습 초점
---------
join이 요구하는 문자열 원소 타입

구현할 함수
-----------
def join_as_text(values: list[object], separator: str) -> str:

예시 및 필수 테스트
-------------------
- join_as_text([1, True, 'x'], ',') == '1,True,x'
- join_as_text([], ',') == ''
- join_as_text([None], '-') == 'None'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0148 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def join_as_text(values: list[object], separator: str) -> str:
    raise NotImplementedError("TODO: PB0148")


def self_test() -> None:
    assert join_as_text([1, True, 'x'], ',') == '1,True,x'
    assert join_as_text([], ',') == ''
    assert join_as_text([None], '-') == 'None'
