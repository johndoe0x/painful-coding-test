"""
PB0283 — 지역 문자열 복사

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
원본 매개변수는 그대로 두고 지역 변수에 대문자 문자열을 만들어 (원본, 대문자)를 반환한다.

연습 초점
---------
지역 변수 변경이 입력 이름을 바꾸지 않음

구현할 함수
-----------
def uppercase_copy_local(text: str) -> tuple[str, str]:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- uppercase_copy_local('Ada') == ('Ada', 'ADA')
- uppercase_copy_local('') == ('', '')
- uppercase_copy_local('a1') == ('a1', 'A1')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0283 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def uppercase_copy_local(text: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0283")


def self_test() -> None:
    assert uppercase_copy_local('Ada') == ('Ada', 'ADA')
    assert uppercase_copy_local('') == ('', '')
    assert uppercase_copy_local('a1') == ('a1', 'A1')
