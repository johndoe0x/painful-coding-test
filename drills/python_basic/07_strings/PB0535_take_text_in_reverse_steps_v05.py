"""
PB0535 — 뒤에서 간격을 두고 읽기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
step이 양수라고 가정하고 마지막 글자부터 왼쪽으로 step칸씩 이동한 글자를 반환한다.

연습 초점
---------
음수 슬라이스 보폭을 동적으로 구성한다.

구현할 함수
-----------
def reverse_step_text(text: str, step: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- reverse_step_text('abcdef', 2) == 'fdb'
- reverse_step_text('abcdefg', 3) == 'gda'
- reverse_step_text('', 2) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0535 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_step_text(text: str, step: int) -> str:
    raise NotImplementedError("TODO: PB0535")


def self_test() -> None:
    assert reverse_step_text('abcdef', 2) == 'fdb'
    assert reverse_step_text('abcdefg', 3) == 'gda'
    assert reverse_step_text('', 2) == ''
