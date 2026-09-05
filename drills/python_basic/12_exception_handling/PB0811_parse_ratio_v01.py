"""
PB0811 — 두 예외를 나눈 비율 파싱

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
int 변환의 ValueError와 나눗셈의 ZeroDivisionError를 별도 except 블록으로 처리하고 둘 다 None을 반환한다.

연습 초점
---------
여러 except 블록의 기본 형태

구현할 함수
-----------
def parse_ratio(left: str, right: str) -> float | None:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- parse_ratio('6', '2') == 3.0
- parse_ratio('x', '2') is None
- parse_ratio('1', '0') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0811 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def parse_ratio(left: str, right: str) -> float | None:
    raise NotImplementedError("TODO: PB0811")


def self_test() -> None:
    assert parse_ratio('6', '2') == 3.0
    assert parse_ratio('x', '2') is None
    assert parse_ratio('1', '0') is None
