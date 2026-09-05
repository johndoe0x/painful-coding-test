"""
PB0472 — 더 긴 문자열 고르기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 문자열 중 길이가 더 긴 것을 반환하고, 길이가 같으면 left를 반환한다.

연습 초점
---------
각 문자열의 길이를 비교하고 동률 규칙을 적용한다.

구현할 함수
-----------
def longer_text(left: str, right: str) -> str:

예시 및 필수 테스트
-------------------
- longer_text('cat', 'python') == 'python'
- longer_text('same', 'size') == 'same'
- longer_text('', 'a') == 'a'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0472 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def longer_text(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0472")


def self_test() -> None:
    assert longer_text('cat', 'python') == 'python'
    assert longer_text('same', 'size') == 'same'
    assert longer_text('', 'a') == 'a'
