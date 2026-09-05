"""
PB0516 — 구분자를 넣어 반복하기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
count는 0 이상이라고 가정한다. text를 count번 연결하고 각 복사본 사이에만 separator를 넣으며 count가 0이면 ''를 반환한다.

연습 초점
---------
반복 결합에서 마지막 뒤의 불필요한 구분자를 피한다.

구현할 함수
-----------
def repeat_with_separator(text: str, count: int, separator: str) -> str:

예시 및 필수 테스트
-------------------
- repeat_with_separator('ha', 3, '-') == 'ha-ha-ha'
- repeat_with_separator('x', 1, ',') == 'x'
- repeat_with_separator('x', 0, ',') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0516 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_with_separator(text: str, count: int, separator: str) -> str:
    raise NotImplementedError("TODO: PB0516")


def self_test() -> None:
    assert repeat_with_separator('ha', 3, '-') == 'ha-ha-ha'
    assert repeat_with_separator('x', 1, ',') == 'x'
    assert repeat_with_separator('x', 0, ',') == ''
