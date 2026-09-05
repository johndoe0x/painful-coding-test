"""
PB0498 — 이웃한 글자 쌍 만들기

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: for

문제
----
서로 이웃한 두 글자를 이어 붙인 문자열들을 순서대로 반환한다.

연습 초점
---------
인덱스 반복 범위를 마지막 이전 위치까지만 설정한다.

구현할 함수
-----------
def adjacent_character_pairs(text: str) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- adjacent_character_pairs('abcd') == ['ab', 'bc', 'cd']
- adjacent_character_pairs('a') == []
- adjacent_character_pairs('') == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0498 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def adjacent_character_pairs(text: str) -> list[str]:
    raise NotImplementedError("TODO: PB0498")


def self_test() -> None:
    assert adjacent_character_pairs('abcd') == ['ab', 'bc', 'cd']
    assert adjacent_character_pairs('a') == []
    assert adjacent_character_pairs('') == []
