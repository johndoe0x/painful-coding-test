"""
PB0122 — 재할당 전후 타입

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 slot 변수에 first를 할당한 타입과 second로 재할당한 타입을 tuple로 반환하세요.

연습 초점
---------
변수 이름이 아닌 현재 값의 타입

구현할 함수
-----------
def rebinding_types(first: object, second: object) -> tuple[str, str]:

예시 및 필수 테스트
-------------------
- rebinding_types(1, 'one') == ('int', 'str')
- rebinding_types(None, None) == ('NoneType', 'NoneType')
- rebinding_types(False, 0) == ('bool', 'int')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0122 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rebinding_types(first: object, second: object) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0122")


def self_test() -> None:
    assert rebinding_types(1, 'one') == ('int', 'str')
    assert rebinding_types(None, None) == ('NoneType', 'NoneType')
    assert rebinding_types(False, 0) == ('bool', 'int')
