"""
PB0383 — while 문자열 반복

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while을 사용해 marker를 count번 이어 붙이며 count가 0 이하면 빈 문자열을 반환한다.

연습 초점
---------
반복 횟수와 while 카운터 갱신

구현할 함수
-----------
def repeat_marker_while(marker: str, count: int) -> str:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- repeat_marker_while('ab', 3) == 'ababab'
- repeat_marker_while('x', 0) == ''
- repeat_marker_while('', 5) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0383 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_marker_while(marker: str, count: int) -> str:
    raise NotImplementedError("TODO: PB0383")


def self_test() -> None:
    assert repeat_marker_while('ab', 3) == 'ababab'
    assert repeat_marker_while('x', 0) == ''
    assert repeat_marker_while('', 5) == ''
