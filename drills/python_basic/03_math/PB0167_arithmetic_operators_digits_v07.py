"""
PB0167 — 두 자리 숫자 분해

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
0~99인 number의 십의 자리와 일의 자리를 반환하세요.

연습 초점
---------
정수 나눗셈과 나머지로 자릿수 추출

구현할 함수
-----------
def split_two_digits(number: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- split_two_digits(42) == (4, 2)
- split_two_digits(0) == (0, 0)
- split_two_digits(99) == (9, 9)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0167 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_two_digits(number: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0167")


def self_test() -> None:
    assert split_two_digits(42) == (4, 2)
    assert split_two_digits(0) == (0, 0)
    assert split_two_digits(99) == (9, 9)
