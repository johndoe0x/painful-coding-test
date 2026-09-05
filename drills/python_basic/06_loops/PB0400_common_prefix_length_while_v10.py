"""
PB0400 — 공통 접두부 길이

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: while

문제
----
두 문자열의 같은 위치 문자가 일치하는 동안 while로 이동해 공통 접두부 길이를 반환한다.

연습 초점
---------
두 입력 경계와 카운터 동기화

구현할 함수
-----------
def common_prefix_length_while(left: str, right: str) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- common_prefix_length_while('flower', 'flow') == 4
- common_prefix_length_while('', 'x') == 0
- common_prefix_length_while('abc', 'xyz') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0400 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def common_prefix_length_while(left: str, right: str) -> int:
    raise NotImplementedError("TODO: PB0400")


def self_test() -> None:
    assert common_prefix_length_while('flower', 'flow') == 4
    assert common_prefix_length_while('', 'x') == 0
    assert common_prefix_length_while('abc', 'xyz') == 0
