"""
PB0609 — 중복 원소 존재 확인하기

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 정수가 두 번 이상 나타나면 True를 반환한다.

연습 초점
---------
전체 길이와 set으로 만든 고유 원소 수를 비교한다.

구현할 함수
-----------
def has_duplicate_value(values: list[int]) -> bool:

예시 및 필수 테스트
-------------------
- has_duplicate_value([1, 2, 1]) is True
- has_duplicate_value([1, 2, 3]) is False
- has_duplicate_value([]) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0609 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_duplicate_value(values: list[int]) -> bool:
    raise NotImplementedError("TODO: PB0609")


def self_test() -> None:
    assert has_duplicate_value([1, 2, 1]) is True
    assert has_duplicate_value([1, 2, 3]) is False
    assert has_duplicate_value([]) is False
