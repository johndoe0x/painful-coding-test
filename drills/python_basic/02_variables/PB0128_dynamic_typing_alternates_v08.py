"""
PB0128 — 타입 번갈음 검사

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 인접 값의 실제 타입이 서로 다르면 True를 반환하세요. 길이 0 또는 1도 True입니다.

연습 초점
---------
연속 재할당의 타입 패턴

구현할 함수
-----------
def types_alternate(values: list[object]) -> bool:

예시 및 필수 테스트
-------------------
- types_alternate([1, 'a', 2]) is True
- types_alternate([]) is True
- types_alternate([1, 2]) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0128 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def types_alternate(values: list[object]) -> bool:
    raise NotImplementedError("TODO: PB0128")


def self_test() -> None:
    assert types_alternate([1, 'a', 2]) is True
    assert types_alternate([]) is True
    assert types_alternate([1, 2]) is False
