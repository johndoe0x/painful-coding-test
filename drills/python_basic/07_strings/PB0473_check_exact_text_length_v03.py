"""
PB0473 — 정확한 길이 확인하기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
text의 길이가 expected와 정확히 같을 때만 True를 반환한다.

연습 초점
---------
len의 결과를 정수 조건과 비교한다.

구현할 함수
-----------
def has_exact_length(text: str, expected: int) -> bool:

예시 및 필수 테스트
-------------------
- has_exact_length('code', 4) is True
- has_exact_length('code', 3) is False
- has_exact_length('', 0) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0473 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_exact_length(text: str, expected: int) -> bool:
    raise NotImplementedError("TODO: PB0473")


def self_test() -> None:
    assert has_exact_length('code', 4) is True
    assert has_exact_length('code', 3) is False
    assert has_exact_length('', 0) is True
