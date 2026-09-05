"""
PB0062 — 가로세로 기록

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
가로·세로·넓이를 각각 변수로 선언해 {'width': ..., 'height': ..., 'area': ...}를 반환하세요.

연습 초점
---------
계산 중간값에 의미 부여

구현할 함수
-----------
def declare_rectangle(width: float, height: float) -> dict[str, float]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_rectangle(3, 4) == {'width': 3, 'height': 4, 'area': 12}
- declare_rectangle(0, 5) == {'width': 0, 'height': 5, 'area': 0}
- declare_rectangle(0.5, 2) == {'width': 0.5, 'height': 2, 'area': 1.0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0062 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_rectangle(width: float, height: float) -> dict[str, float]:
    raise NotImplementedError("TODO: PB0062")


def self_test() -> None:
    assert declare_rectangle(3, 4) == {'width': 3, 'height': 4, 'area': 12}
    assert declare_rectangle(0, 5) == {'width': 0, 'height': 5, 'area': 0}
    assert declare_rectangle(0.5, 2) == {'width': 0.5, 'height': 2, 'area': 1.0}
