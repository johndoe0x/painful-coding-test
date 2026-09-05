"""
PB0312 — 문자열 길이 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
left가 더 짧으면 -1, 길이가 같으면 0, 더 길면 1을 반환한다.

연습 초점
---------
계산값 사이의 대소 비교

구현할 함수
-----------
def compare_text_lengths(left: str, right: str) -> int:

예시 및 필수 테스트
-------------------
- compare_text_lengths('cat', 'python') == -1
- compare_text_lengths('ab', '한글') == 0
- compare_text_lengths('long', '') == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0312 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def compare_text_lengths(left: str, right: str) -> int:
    raise NotImplementedError("TODO: PB0312")


def self_test() -> None:
    assert compare_text_lengths('cat', 'python') == -1
    assert compare_text_lengths('ab', '한글') == 0
    assert compare_text_lengths('long', '') == 1
