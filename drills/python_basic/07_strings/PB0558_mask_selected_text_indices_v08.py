"""
PB0558 — 선택 위치 가리기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
indices에는 유효한 0 이상 인덱스가 들어 있고 mask는 한 글자라고 가정해 지정 위치들을 mask로 바꾼 새 문자열을 반환한다.

연습 초점
---------
원본을 보존하면서 여러 위치를 변경 가능한 복사본에 반영한다.

구현할 함수
-----------
def mask_text_indices(text: str, indices: list[int], mask: str) -> str:

예시 및 필수 테스트
-------------------
- mask_text_indices('secret', [1, 3], '*') == 's*c*et'
- mask_text_indices('abc', [], '#') == 'abc'
- mask_text_indices('aaa', [0, 1, 2], '-') == '---'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0558 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mask_text_indices(text: str, indices: list[int], mask: str) -> str:
    raise NotImplementedError("TODO: PB0558")


def self_test() -> None:
    assert mask_text_indices('secret', [1, 3], '*') == 's*c*et'
    assert mask_text_indices('abc', [], '#') == 'abc'
    assert mask_text_indices('aaa', [0, 1, 2], '-') == '---'
