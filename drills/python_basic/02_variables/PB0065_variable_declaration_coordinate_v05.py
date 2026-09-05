"""
PB0065 — 좌표 변수 묶기

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
x와 y를 변수로 유지하고 둘 다 0이면 'origin', 아니면 'point'라는 label을 선언해 함께 반환하세요.

연습 초점
---------
값에서 파생한 상태 변수

구현할 함수
-----------
def declare_coordinate(x: int, y: int) -> tuple[int, int, str]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_coordinate(2, 3) == (2, 3, 'point')
- declare_coordinate(0, 0) == (0, 0, 'origin')
- declare_coordinate(0, 5) == (0, 5, 'point')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0065 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_coordinate(x: int, y: int) -> tuple[int, int, str]:
    raise NotImplementedError("TODO: PB0065")


def self_test() -> None:
    assert declare_coordinate(2, 3) == (2, 3, 'point')
    assert declare_coordinate(0, 0) == (0, 0, 'origin')
    assert declare_coordinate(0, 5) == (0, 5, 'point')
