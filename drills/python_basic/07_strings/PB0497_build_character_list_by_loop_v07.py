"""
PB0497 — 반복문으로 글자 리스트 만들기

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for

문제
----
list(text)를 사용하지 말고 문자열을 순회해 한 글자씩 리스트에 담는다.

연습 초점
---------
for 반복과 append로 문자열을 리스트로 변환한다.

구현할 함수
-----------
def collect_characters(text: str) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- collect_characters('dog') == ['d', 'o', 'g']
- collect_characters(' ') == [' ']
- collect_characters('') == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0497 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def collect_characters(text: str) -> list[str]:
    raise NotImplementedError("TODO: PB0497")


def self_test() -> None:
    assert collect_characters('dog') == ['d', 'o', 'g']
    assert collect_characters(' ') == [' ']
    assert collect_characters('') == []
