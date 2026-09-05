"""
PB0382 — 목표까지 한 칸 이동

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while을 사용해 start에서 target 방향으로 한 칸씩 이동하며 start 다음 값부터 target까지 반환한다.

연습 초점
---------
상태에 따라 증가 또는 감소하는 while

구현할 함수
-----------
def walk_to_target_while(start: int, target: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- walk_to_target_while(2, 5) == [3, 4, 5]
- walk_to_target_while(5, 2) == [4, 3, 2]
- walk_to_target_while(3, 3) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0382 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def walk_to_target_while(start: int, target: int) -> list[int]:
    raise NotImplementedError("TODO: PB0382")


def self_test() -> None:
    assert walk_to_target_while(2, 5) == [3, 4, 5]
    assert walk_to_target_while(5, 2) == [4, 3, 2]
    assert walk_to_target_while(3, 3) == []
