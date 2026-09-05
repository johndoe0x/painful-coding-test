"""
PB0071 — 의미 있는 이름 합치기

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
의미가 드러나는 변수명을 사용해 두 이름을 공백 하나로 결합하세요.

연습 초점
---------
snake_case와 구체적인 변수명

구현할 함수
-----------
def join_name(first_name: str, last_name: str) -> str:

예시 및 필수 테스트
-------------------
- join_name('Ada', 'Lovelace') == 'Ada Lovelace'
- join_name('', '') == ' '
- join_name('A', 'B') == 'A B'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0071 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def join_name(first_name: str, last_name: str) -> str:
    raise NotImplementedError("TODO: PB0071")


def self_test() -> None:
    assert join_name('Ada', 'Lovelace') == 'Ada Lovelace'
    assert join_name('', '') == ' '
    assert join_name('A', 'B') == 'A B'
