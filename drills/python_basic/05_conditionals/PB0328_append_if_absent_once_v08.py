"""
PB0328 — 없는 값만 추가

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: if

문제
----
리스트 복사본을 만들고 item이 없을 때만 끝에 한 번 추가한다.

연습 초점
---------
멤버십 조건의 단일 if

구현할 함수
-----------
def append_if_absent_once(values: list[int], item: int) -> list[int]:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- append_if_absent_once([1, 2], 3) == [1, 2, 3]
- append_if_absent_once([1, 2], 2) == [1, 2]
- append_if_absent_once([], -1) == [-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0328 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_if_absent_once(values: list[int], item: int) -> list[int]:
    raise NotImplementedError("TODO: PB0328")


def self_test() -> None:
    assert append_if_absent_once([1, 2], 3) == [1, 2, 3]
    assert append_if_absent_once([1, 2], 2) == [1, 2]
    assert append_if_absent_once([], -1) == [-1]
