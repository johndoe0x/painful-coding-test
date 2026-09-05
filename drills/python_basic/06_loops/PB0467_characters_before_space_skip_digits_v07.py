"""
PB0467 — 공백 전 비숫자 문자

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
문자를 순회하다 공백에서 break하고 숫자는 continue해 그전 비숫자 문자만 이어 붙인다.

연습 초점
---------
문자 단위 break·continue

구현할 함수
-----------
def characters_before_space_skip_digits(text: str) -> str:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- characters_before_space_skip_digits('a1b2 c3') == 'ab'
- characters_before_space_skip_digits('123') == ''
- characters_before_space_skip_digits(' abc') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0467 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def characters_before_space_skip_digits(text: str) -> str:
    raise NotImplementedError("TODO: PB0467")


def self_test() -> None:
    assert characters_before_space_skip_digits('a1b2 c3') == 'ab'
    assert characters_before_space_skip_digits('123') == ''
    assert characters_before_space_skip_digits(' abc') == ''
