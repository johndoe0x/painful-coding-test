"""
PB0093 — 격자 위치 갱신

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
start를 x, y로 두고 각 move가 'N'이면 y += 1, 'S'이면 y -= 1, 'E'이면 x += 1, 'W'이면 x -= 1로 순서대로 재할당해 최종 좌표를 반환하세요. moves에는 이 네 값만 들어옵니다.

연습 초점
---------
두 상태 변수를 방향 명령에 따라 재할당

구현할 함수
-----------
def move_grid_position(start: tuple[int, int], moves: list[str]) -> tuple[int, int]:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- move_grid_position((0, 0), ['N', 'E', 'E']) == (2, 1)
- move_grid_position((3, -1), ['W', 'S']) == (2, -2)
- move_grid_position((5, 5), []) == (5, 5)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0093 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def move_grid_position(start: tuple[int, int], moves: list[str]) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0093")


def self_test() -> None:
    assert move_grid_position((0, 0), ['N', 'E', 'E']) == (2, 1)
    assert move_grid_position((3, -1), ['W', 'S']) == (2, -2)
    assert move_grid_position((5, 5), []) == (5, 5)
