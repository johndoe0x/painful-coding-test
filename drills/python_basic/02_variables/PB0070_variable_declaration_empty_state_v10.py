"""
PB0070 — 빈 초기 상태

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
빈 문자열 name, 0인 count, 빈 리스트 items를 각각 변수로 선언해 딕셔너리로 반환하세요.

연습 초점
---------
타입별 초기값 선언

구현할 함수
-----------
def declare_empty_state() -> dict[str, object]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_empty_state() == {'name': '', 'count': 0, 'items': []}
- declare_empty_state()['items'] == []
- declare_empty_state() is not declare_empty_state()

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0070 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_empty_state() -> dict[str, object]:
    raise NotImplementedError("TODO: PB0070")


def self_test() -> None:
    assert declare_empty_state() == {'name': '', 'count': 0, 'items': []}
    assert declare_empty_state()['items'] == []
    assert declare_empty_state() is not declare_empty_state()
