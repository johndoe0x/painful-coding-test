"""
PB0224 — 해시태그 생성 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열 앞에 '#'을 붙여 반환한다.

연습 초점
---------
문자열을 가공하는 함수의 입출력

구현할 함수
-----------
def make_hash_tag(word: str) -> str:

예시 및 필수 테스트
-------------------
- make_hash_tag('python') == '#python'
- make_hash_tag('') == '#'
- make_hash_tag('AI') == '#AI'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0224 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_hash_tag(word: str) -> str:
    raise NotImplementedError("TODO: PB0224")


def self_test() -> None:
    assert make_hash_tag('python') == '#python'
    assert make_hash_tag('') == '#'
    assert make_hash_tag('AI') == '#AI'
