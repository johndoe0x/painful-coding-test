"""
PB0346 — 더 긴 문자열 선택

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
left가 더 길면 left, 아니면 right를 반환한다.

연습 초점
---------
길이 비교에 따른 두 반환 경로

구현할 함수
-----------
def longer_text_or_right(left: str, right: str) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- longer_text_or_right('python', 'go') == 'python'
- longer_text_or_right('a', 'ruby') == 'ruby'
- longer_text_or_right('ab', 'cd') == 'cd'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0346 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def longer_text_or_right(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0346")


def self_test() -> None:
    assert longer_text_or_right('python', 'go') == 'python'
    assert longer_text_or_right('a', 'ruby') == 'ruby'
    assert longer_text_or_right('ab', 'cd') == 'cd'
