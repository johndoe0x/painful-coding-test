"""
PB0418 — for 글자 개수

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: for

문제
----
한 글자인 target과 같은 문자를 for로 순회하며 센다.

연습 초점
---------
문자열 직접 순회와 카운터

구현할 함수
-----------
def count_letter_for(text: str, target: str) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- count_letter_for('banana', 'a') == 3
- count_letter_for('', 'x') == 0
- count_letter_for('AAA', 'a') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0418 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_letter_for(text: str, target: str) -> int:
    raise NotImplementedError("TODO: PB0418")


def self_test() -> None:
    assert count_letter_for('banana', 'a') == 3
    assert count_letter_for('', 'x') == 0
    assert count_letter_for('AAA', 'a') == 0
