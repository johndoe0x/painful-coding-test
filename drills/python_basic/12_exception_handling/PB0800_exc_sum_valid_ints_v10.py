"""
PB0800 — 변환 가능한 정수만 합산

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: try

문제
----
각 문자열을 int로 변환해 더하고 ValueError가 난 항목만 건너뛴다.

연습 초점
---------
반복문 내부의 좁은 try-except

구현할 함수
-----------
def exc_sum_valid_ints(texts: list[str]) -> int:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_sum_valid_ints(['1', 'x', '2']) == 3
- exc_sum_valid_ints([]) == 0
- exc_sum_valid_ints(['bad']) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0800 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_sum_valid_ints(texts: list[str]) -> int:
    raise NotImplementedError("TODO: PB0800")


def self_test() -> None:
    assert exc_sum_valid_ints(['1', 'x', '2']) == 3
    assert exc_sum_valid_ints([]) == 0
    assert exc_sum_valid_ints(['bad']) == 0
