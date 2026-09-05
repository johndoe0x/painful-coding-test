"""
PB0546 — 앞부분만 뒤집기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
size가 0 이상이라고 가정해 앞 size글자만 뒤집고 나머지는 원래 순서로 둔다.

연습 초점
---------
앞부분 슬라이스를 역순으로 바꾼 뒤 뒤쪽 슬라이스와 연결한다.

구현할 함수
-----------
def reverse_prefix(text: str, size: int) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_prefix('abcdef', 3) == 'cbadef'
- reverse_prefix('abc', 8) == 'cba'
- reverse_prefix('abc', 0) == 'abc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0546 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_prefix(text: str, size: int) -> str:
    raise NotImplementedError("TODO: PB0546")


def self_test() -> None:
    assert reverse_prefix('abcdef', 3) == 'cbadef'
    assert reverse_prefix('abc', 8) == 'cba'
    assert reverse_prefix('abc', 0) == 'abc'
