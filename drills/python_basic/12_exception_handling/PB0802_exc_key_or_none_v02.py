"""
PB0802 — 안전한 딕셔너리 대괄호 조회

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: try

문제
----
mapping[key]를 반환하고 KeyError면 None을 반환한다.

연습 초점
---------
KeyError가 발생하는 표현식 식별

구현할 함수
-----------
def exc_key_or_none(mapping: dict[str, object], key: str) -> object | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_key_or_none({'a': 1}, 'a') == 1
- exc_key_or_none({'a': 1}, 'x') is None
- exc_key_or_none({}, '') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0802 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_key_or_none(mapping: dict[str, object], key: str) -> object | None:
    raise NotImplementedError("TODO: PB0802")


def self_test() -> None:
    assert exc_key_or_none({'a': 1}, 'a') == 1
    assert exc_key_or_none({'a': 1}, 'x') is None
    assert exc_key_or_none({}, '') is None
