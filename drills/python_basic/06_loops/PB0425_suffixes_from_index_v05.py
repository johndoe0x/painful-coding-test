"""
PB0425 — 시작 위치 이후 접미사

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(text)라고 가정하고 for와 range(start, len(text))로 각 인덱스에서 시작하는 접미사를 반환한다.

연습 초점
---------
유효한 시작 인덱스와 슬라이싱 결합

구현할 함수
-----------
def suffixes_from_index(text: str, start: int) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- suffixes_from_index('abcd', 2) == ['cd', 'd']
- suffixes_from_index('abc', 3) == []
- suffixes_from_index('x', 0) == ['x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0425 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def suffixes_from_index(text: str, start: int) -> list[str]:
    raise NotImplementedError("TODO: PB0425")


def self_test() -> None:
    assert suffixes_from_index('abcd', 2) == ['cd', 'd']
    assert suffixes_from_index('abc', 3) == []
    assert suffixes_from_index('x', 0) == ['x']
