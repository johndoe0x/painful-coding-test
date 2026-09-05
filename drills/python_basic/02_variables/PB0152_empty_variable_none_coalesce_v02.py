"""
PB0152 — None만 대체

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 정확히 None일 때만 default를 반환하고 0, False, 빈 문자열은 그대로 반환하세요.

연습 초점
---------
None과 일반적인 falsy 값 구분

구현할 함수
-----------
def coalesce_none(value: object | None, default: object) -> object:

예시 및 필수 테스트
-------------------
- coalesce_none(None, 'x') == 'x'
- coalesce_none(0, 9) == 0
- coalesce_none('', 'fallback') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0152 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def coalesce_none(value: object | None, default: object) -> object:
    raise NotImplementedError("TODO: PB0152")


def self_test() -> None:
    assert coalesce_none(None, 'x') == 'x'
    assert coalesce_none(0, 9) == 0
    assert coalesce_none('', 'fallback') == ''
