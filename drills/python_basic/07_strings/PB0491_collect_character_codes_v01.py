"""
PB0491 — 문자 코드 모으기

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for

문제
----
text를 왼쪽부터 순회하며 각 문자의 ord 값을 리스트로 반환한다.

연습 초점
---------
문자열 for 순회와 ord 호출을 연습한다.

구현할 함수
-----------
def char_codes(text: str) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- char_codes('AB') == [65, 66]
- char_codes('a!') == [97, 33]
- char_codes('') == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0491 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def char_codes(text: str) -> list[int]:
    raise NotImplementedError("TODO: PB0491")


def self_test() -> None:
    assert char_codes('AB') == [65, 66]
    assert char_codes('a!') == [97, 33]
    assert char_codes('') == []
