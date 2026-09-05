"""
PB0054 — 도형 계산 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
넓이와 둘레를 {'area': ..., 'perimeter': ...}로 반환하고 공식 선택 이유를 주석으로 작성하세요.

연습 초점
---------
계산 의도를 설명하는 짧은 주석

구현할 함수
-----------
def rectangle_metrics(width: float, height: float) -> dict[str, float]:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- rectangle_metrics(3, 4) == {'area': 12, 'perimeter': 14}
- rectangle_metrics(0, 5) == {'area': 0, 'perimeter': 10}
- rectangle_metrics(1, 1) == {'area': 1, 'perimeter': 4}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0054 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rectangle_metrics(width: float, height: float) -> dict[str, float]:
    raise NotImplementedError("TODO: PB0054")


def self_test() -> None:
    assert rectangle_metrics(3, 4) == {'area': 12, 'perimeter': 14}
    assert rectangle_metrics(0, 5) == {'area': 0, 'perimeter': 10}
    assert rectangle_metrics(1, 1) == {'area': 1, 'perimeter': 4}
