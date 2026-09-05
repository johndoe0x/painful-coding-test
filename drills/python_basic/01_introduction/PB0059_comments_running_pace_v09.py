"""
PB0059 — 페이스 단위 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
총 minutes를 kilometers로 나눈 km당 분을 반환하고 결과 단위를 주석으로 적으세요. kilometers는 양수입니다.

연습 초점
---------
반환값 단위를 명확히 하는 주석

구현할 함수
-----------
def pace_per_kilometer(minutes: float, kilometers: float) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- pace_per_kilometer(50, 10) == 5.0
- pace_per_kilometer(0, 5) == 0.0
- pace_per_kilometer(7.5, 1) == 7.5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0059 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pace_per_kilometer(minutes: float, kilometers: float) -> float:
    raise NotImplementedError("TODO: PB0059")


def self_test() -> None:
    assert pace_per_kilometer(50, 10) == 5.0
    assert pace_per_kilometer(0, 5) == 0.0
    assert pace_per_kilometer(7.5, 1) == 7.5
