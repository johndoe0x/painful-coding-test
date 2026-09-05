"""
PB0055 — 시간 변환 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
seconds를 (온전한 분, 남은 초)로 반환하고 60으로 나누는 이유를 주석으로 작성하세요.

연습 초점
---------
단위 변환을 설명하는 주석

구현할 함수
-----------
def seconds_to_minutes(seconds: int) -> tuple[int, int]:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- seconds_to_minutes(125) == (2, 5)
- seconds_to_minutes(0) == (0, 0)
- seconds_to_minutes(60) == (1, 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0055 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def seconds_to_minutes(seconds: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0055")


def self_test() -> None:
    assert seconds_to_minutes(125) == (2, 5)
    assert seconds_to_minutes(0) == (0, 0)
    assert seconds_to_minutes(60) == (1, 0)
