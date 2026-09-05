"""
PB0305 — 기본 반복 횟수

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
text를 count번 반복하며 count 생략 시 두 번 반복한다.

연습 초점
---------
선택적 설정 매개변수

구현할 함수
-----------
def repeat_with_default(text: str, count: int = 2) -> str:

예시 및 필수 테스트
-------------------
- repeat_with_default('ha') == 'haha'
- repeat_with_default('x', 3) == 'xxx'
- repeat_with_default('', 5) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0305 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_with_default(text: str, count: int = 2) -> str:
    raise NotImplementedError("TODO: PB0305")


def self_test() -> None:
    assert repeat_with_default('ha') == 'haha'
    assert repeat_with_default('x', 3) == 'xxx'
    assert repeat_with_default('', 5) == ''
