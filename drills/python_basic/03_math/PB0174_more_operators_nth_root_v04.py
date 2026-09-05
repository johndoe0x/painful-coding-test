"""
PB0174 — n제곱근

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
0 이상 value와 양수 degree에 대해 value ** (1 / degree)를 반환하세요.

연습 초점
---------
분수 지수를 사용한 거듭제곱근

구현할 함수
-----------
def nth_root(value: float, degree: int) -> float:

예시 및 필수 테스트
-------------------
- nth_root(16, 2) == 4.0
- nth_root(0, 3) == 0.0
- nth_root(27, 3) == 3.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0174 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def nth_root(value: float, degree: int) -> float:
    raise NotImplementedError("TODO: PB0174")


def self_test() -> None:
    assert nth_root(16, 2) == 4.0
    assert nth_root(0, 3) == 0.0
    assert nth_root(27, 3) == 3.0
