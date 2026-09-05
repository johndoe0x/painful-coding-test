"""
PB0095 — 문자열 이어 붙이기

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
result 변수를 각 fragment와 차례로 이어 붙여 반환하세요.

연습 초점
---------
불변 문자열 변수의 재할당

구현할 함수
-----------
def append_fragments(prefix: str, fragments: list[str]) -> str:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- append_fragments('a', ['b', 'c']) == 'abc'
- append_fragments('', []) == ''
- append_fragments('', ['x']) == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0095 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_fragments(prefix: str, fragments: list[str]) -> str:
    raise NotImplementedError("TODO: PB0095")


def self_test() -> None:
    assert append_fragments('a', ['b', 'c']) == 'abc'
    assert append_fragments('', []) == ''
    assert append_fragments('', ['x']) == 'x'
