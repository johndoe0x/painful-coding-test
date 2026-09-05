"""
PB0486 — 여러 위치의 글자 고르기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 indices가 text의 유효한 인덱스라고 가정하고 해당 글자들을 순서대로 이어 반환한다.

연습 초점
---------
인덱스 리스트를 순회하며 문자열에서 선택한다.

구현할 함수
-----------
def characters_at(text: str, indices: list[int]) -> str:

예시 및 필수 테스트
-------------------
- characters_at('python', [0, 2, 5]) == 'ptn'
- characters_at('abc', [-1, 0]) == 'ca'
- characters_at('hello', []) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0486 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def characters_at(text: str, indices: list[int]) -> str:
    raise NotImplementedError("TODO: PB0486")


def self_test() -> None:
    assert characters_at('python', [0, 2, 5]) == 'ptn'
    assert characters_at('abc', [-1, 0]) == 'ca'
    assert characters_at('hello', []) == ''
