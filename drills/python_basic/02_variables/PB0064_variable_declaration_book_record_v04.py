"""
PB0064 — 책 정보 변수

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
책 제목과 쪽수를 변수로 선언하고 쪽수가 0보다 큰지도 is_nonempty 키에 담아 반환하세요.

연습 초점
---------
서로 다른 타입의 변수 구성

구현할 함수
-----------
def declare_book(title: str, pages: int) -> dict[str, object]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_book('Python', 300) == {'title': 'Python', 'pages': 300, 'is_nonempty': True}
- declare_book('', 0) == {'title': '', 'pages': 0, 'is_nonempty': False}
- declare_book('A', 1) == {'title': 'A', 'pages': 1, 'is_nonempty': True}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0064 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_book(title: str, pages: int) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0064")


def self_test() -> None:
    assert declare_book('Python', 300) == {'title': 'Python', 'pages': 300, 'is_nonempty': True}
    assert declare_book('', 0) == {'title': '', 'pages': 0, 'is_nonempty': False}
    assert declare_book('A', 1) == {'title': 'A', 'pages': 1, 'is_nonempty': True}
