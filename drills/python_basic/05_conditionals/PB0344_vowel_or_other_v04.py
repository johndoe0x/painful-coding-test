"""
PB0344 — 모음 여부 구분

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
한 글자가 영문 모음이면 'vowel', 아니면 'other'를 반환한다.

연습 초점
---------
멤버십 조건의 if-else

구현할 함수
-----------
def vowel_or_other(character: str) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- vowel_or_other('a') == 'vowel'
- vowel_or_other('E') == 'vowel'
- vowel_or_other('z') == 'other'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0344 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def vowel_or_other(character: str) -> str:
    raise NotImplementedError("TODO: PB0344")


def self_test() -> None:
    assert vowel_or_other('a') == 'vowel'
    assert vowel_or_other('E') == 'vowel'
    assert vowel_or_other('z') == 'other'
