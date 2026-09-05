"""
PB0550 — 서로 역순인 문자열인지 확인하기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
right가 left의 정확한 역순일 때만 True를 반환한다.

연습 초점
---------
한 문자열의 역방향 슬라이스를 다른 문자열과 비교한다.

구현할 함수
-----------
def are_reverse_pair(left: str, right: str) -> bool:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- are_reverse_pair('abc', 'cba') is True
- are_reverse_pair('abc', 'abc') is False
- are_reverse_pair('', '') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0550 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def are_reverse_pair(left: str, right: str) -> bool:
    raise NotImplementedError("TODO: PB0550")


def self_test() -> None:
    assert are_reverse_pair('abc', 'cba') is True
    assert are_reverse_pair('abc', 'abc') is False
    assert are_reverse_pair('', '') is True
