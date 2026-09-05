"""
PB0246 — 범위 라벨 만들기

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 정수를 'start..stop' 형식의 문자열로 반환한다.

연습 초점
---------
위치 인자 순서의 중요성

구현할 함수
-----------
def make_range_label(start: int, stop: int) -> str:

예시 및 필수 테스트
-------------------
- make_range_label(2, 8) == '2..8'
- make_range_label(-3, 3) == '-3..3'
- make_range_label(5, 5) == '5..5'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0246 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_range_label(start: int, stop: int) -> str:
    raise NotImplementedError("TODO: PB0246")


def self_test() -> None:
    assert make_range_label(2, 8) == '2..8'
    assert make_range_label(-3, 3) == '-3..3'
    assert make_range_label(5, 5) == '5..5'
