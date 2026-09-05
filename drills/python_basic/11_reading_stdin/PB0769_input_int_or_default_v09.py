"""
PB0769 — 잘못된 정수의 기본값

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
int 변환에 실패하면 default를 반환한다.

연습 초점
---------
ValueError 처리와 타입 변환

구현할 함수
-----------
def input_int_or_default(text: str, default: int) -> int:

예시 및 필수 테스트
-------------------
- input_int_or_default('10', 0) == 10
- input_int_or_default('x', 7) == 7
- input_int_or_default('', -1) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0769 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_int_or_default(text: str, default: int) -> int:
    raise NotImplementedError("TODO: PB0769")


def self_test() -> None:
    assert input_int_or_default('10', 0) == 10
    assert input_int_or_default('x', 7) == 7
    assert input_int_or_default('', -1) == -1
