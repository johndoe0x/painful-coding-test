"""
PB0057 — 정산 규칙 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
total을 people명이 똑같이 나눈 1인 금액을 반환하고 균등 분배 규칙을 주석으로 밝히세요. people은 양수입니다.

연습 초점
---------
숨은 정책을 코드 가까이에 기록

구현할 함수
-----------
def split_bill(total: float, people: int) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- split_bill(90, 3) == 30.0
- split_bill(0, 5) == 0.0
- split_bill(10, 1) == 10.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0057 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_bill(total: float, people: int) -> float:
    raise NotImplementedError("TODO: PB0057")


def self_test() -> None:
    assert split_bill(90, 3) == 30.0
    assert split_bill(0, 5) == 0.0
    assert split_bill(10, 1) == 10.0
