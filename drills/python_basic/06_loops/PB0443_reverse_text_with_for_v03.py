"""
PB0443 — for로 문자열 뒤집기

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
마지막 인덱스부터 0까지 for로 순회해 뒤집힌 문자열을 반환한다.

연습 초점
---------
역순 range와 문자열 조립

구현할 함수
-----------
def reverse_text_with_for(text: str) -> str:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_text_with_for('abc') == 'cba'
- reverse_text_with_for('') == ''
- reverse_text_with_for('한글') == '글한'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0443 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_text_with_for(text: str) -> str:
    raise NotImplementedError("TODO: PB0443")


def self_test() -> None:
    assert reverse_text_with_for('abc') == 'cba'
    assert reverse_text_with_for('') == ''
    assert reverse_text_with_for('한글') == '글한'
