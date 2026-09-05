"""
PB0241 — 문자열 반복 매개변수

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
text를 count번 이어 붙인 문자열을 반환한다.

연습 초점
---------
각 매개변수가 결과에 미치는 영향

구현할 함수
-----------
def repeat_text(text: str, count: int) -> str:

예시 및 필수 테스트
-------------------
- repeat_text('ab', 3) == 'ababab'
- repeat_text('x', 0) == ''
- repeat_text('', 5) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0241 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_text(text: str, count: int) -> str:
    raise NotImplementedError("TODO: PB0241")


def self_test() -> None:
    assert repeat_text('ab', 3) == 'ababab'
    assert repeat_text('x', 0) == ''
    assert repeat_text('', 5) == ''
