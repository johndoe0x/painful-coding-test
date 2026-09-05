"""
PB0289 — 지역 온도 변화

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
지역 current에 변화를 적용할 때마다 새 온도를 결과 리스트에 담는다.

연습 초점
---------
지역 상태를 통해 중간 결과 생성

구현할 함수
-----------
def local_temperature_path(start: int, changes: list[int]) -> list[int]:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- local_temperature_path(20, [2, -5]) == [22, 17]
- local_temperature_path(0, []) == []
- local_temperature_path(-3, [3]) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0289 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def local_temperature_path(start: int, changes: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0289")


def self_test() -> None:
    assert local_temperature_path(20, [2, -5]) == [22, 17]
    assert local_temperature_path(0, []) == []
    assert local_temperature_path(-3, [3]) == [0]
