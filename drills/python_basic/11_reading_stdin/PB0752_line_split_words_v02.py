"""
PB0752 — 공백 단어 나누기

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
연속 공백을 하나의 구분으로 보아 단어 목록을 반환한다.

연습 초점
---------
인자 없는 split의 공백 처리

구현할 함수
-----------
def line_split_words(line: str) -> list[str]:

예시 및 필수 테스트
-------------------
- line_split_words('one  two three') == ['one', 'two', 'three']
- line_split_words('   ') == []
- line_split_words('single') == ['single']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0752 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_split_words(line: str) -> list[str]:
    raise NotImplementedError("TODO: PB0752")


def self_test() -> None:
    assert line_split_words('one  two three') == ['one', 'two', 'three']
    assert line_split_words('   ') == []
    assert line_split_words('single') == ['single']
