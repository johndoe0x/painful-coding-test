"""
PB0761 — 정수 입력 변환

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 01 / 10
Time cap: 60 seconds
Source checks:

문제
----
앞뒤 공백이 있을 수 있는 text를 int로 변환한다.

연습 초점
---------
int 생성자의 문자열 변환

구현할 함수
-----------
def parse_int(text: str) -> int:

예시 및 필수 테스트
-------------------
- parse_int(' 12 ') == 12
- parse_int('-1') == -1
- parse_int('0') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0761 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def parse_int(text: str) -> int:
    raise NotImplementedError("TODO: PB0761")


def self_test() -> None:
    assert parse_int(' 12 ') == 12
    assert parse_int('-1') == -1
    assert parse_int('0') == 0
