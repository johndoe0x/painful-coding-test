"""
PB0287 — 지역 일치 횟수

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
함수 내부 count만 갱신해 target의 등장 횟수를 반환한다.

연습 초점
---------
지역 이름이 함수 밖으로 새지 않게 계산

구현할 함수
-----------
def local_match_counter(values: list[str], target: str) -> int:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- local_match_counter(['a', 'b', 'a'], 'a') == 2
- local_match_counter([], 'x') == 0
- local_match_counter(['x'], 'y') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0287 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def local_match_counter(values: list[str], target: str) -> int:
    raise NotImplementedError("TODO: PB0287")


def self_test() -> None:
    assert local_match_counter(['a', 'b', 'a'], 'a') == 2
    assert local_match_counter([], 'x') == 0
    assert local_match_counter(['x'], 'y') == 0
