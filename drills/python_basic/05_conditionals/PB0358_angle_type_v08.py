"""
PB0358 — 각도 종류

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
0 이하는 invalid, 90 미만 acute, 90 right, 180 미만 obtuse, 180 straight, 그 밖 invalid를 반환한다.

연습 초점
---------
동등 조건과 범위 조건을 함께 쓰는 elif

구현할 함수
-----------
def angle_type(degrees: float) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- angle_type(45.0) == 'acute'
- angle_type(90.0) == 'right'
- angle_type(181.0) == 'invalid'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0358 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def angle_type(degrees: float) -> str:
    raise NotImplementedError("TODO: PB0358")


def self_test() -> None:
    assert angle_type(45.0) == 'acute'
    assert angle_type(90.0) == 'right'
    assert angle_type(181.0) == 'invalid'
