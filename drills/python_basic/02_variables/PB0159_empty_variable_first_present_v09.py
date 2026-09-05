"""
PB0159 — 첫 번째 존재하는 값

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
목록에서 처음으로 None이 아닌 값을 반환하고 모두 None이거나 비면 None을 반환하세요.

연습 초점
---------
None을 sentinel로 사용한 탐색

구현할 함수
-----------
def first_present(values: list[object | None]) -> object | None:

예시 및 필수 테스트
-------------------
- first_present([None, 0, 1]) == 0
- first_present([]) is None
- first_present([None, None]) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0159 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_present(values: list[object | None]) -> object | None:
    raise NotImplementedError("TODO: PB0159")


def self_test() -> None:
    assert first_present([None, 0, 1]) == 0
    assert first_present([]) is None
    assert first_present([None, None]) is None
