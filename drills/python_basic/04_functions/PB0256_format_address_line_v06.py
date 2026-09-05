"""
PB0256 — 주소 한 줄 만들기

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
'<city>, <street> <number>' 형식으로 주소를 반환한다.

연습 초점
---------
문자열과 정수 매개변수의 순서

구현할 함수
-----------
def format_address_line(city: str, street: str, number: int) -> str:

예시 및 필수 테스트
-------------------
- format_address_line('Seoul', 'Teheran-ro', 10) == 'Seoul, Teheran-ro 10'
- format_address_line('', 'Main', 0) == ', Main 0'
- format_address_line('Busan', '', 7) == 'Busan,  7'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0256 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_address_line(city: str, street: str, number: int) -> str:
    raise NotImplementedError("TODO: PB0256")


def self_test() -> None:
    assert format_address_line('Seoul', 'Teheran-ro', 10) == 'Seoul, Teheran-ro 10'
    assert format_address_line('', 'Main', 0) == ', Main 0'
    assert format_address_line('Busan', '', 7) == 'Busan,  7'
