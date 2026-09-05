"""
PB0040 — 텍스트 배너

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
text 길이만큼 border의 첫 글자를 반복한 위아래 줄과 text를 줄바꿈으로 연결하세요. border가 비면 '-'를 사용하세요.

연습 초점
---------
동적으로 폭을 맞춘 여러 줄 출력

구현할 함수
-----------
def make_banner(text: str, border: str) -> str:

예시 및 필수 테스트
-------------------
- make_banner('Hi', '*') == '**\\nHi\\n**'
- make_banner('', '#') == '\\n\\n'
- make_banner('A', '') == '-\\nA\\n-'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0040 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_banner(text: str, border: str) -> str:
    raise NotImplementedError("TODO: PB0040")


def self_test() -> None:
    assert make_banner('Hi', '*') == '**\nHi\n**'
    assert make_banner('', '#') == '\n\n'
    assert make_banner('A', '') == '-\nA\n-'
