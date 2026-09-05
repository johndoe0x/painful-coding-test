"""
PB0343 — 두 수 중 큰 값

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
left가 right 이상이면 left, 아니면 right를 반환한다.

연습 초점
---------
if-else에서 하나의 값 선택

구현할 함수
-----------
def larger_of_two(left: int, right: int) -> int:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- larger_of_two(8, 3) == 8
- larger_of_two(2, 9) == 9
- larger_of_two(-4, -4) == -4

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0343 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def larger_of_two(left: int, right: int) -> int:
    raise NotImplementedError("TODO: PB0343")


def self_test() -> None:
    assert larger_of_two(8, 3) == 8
    assert larger_of_two(2, 9) == 9
    assert larger_of_two(-4, -4) == -4
