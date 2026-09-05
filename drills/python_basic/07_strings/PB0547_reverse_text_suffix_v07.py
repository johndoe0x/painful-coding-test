"""
PB0547 — 뒷부분만 뒤집기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
0 <= size <= len(text)라고 가정해 뒤 size글자만 뒤집고 앞부분은 유지한다.

연습 초점
---------
동적 분할 지점 양쪽에서 한쪽에만 역순 슬라이스를 적용한다.

구현할 함수
-----------
def reverse_suffix(text: str, size: int) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_suffix('abcdef', 3) == 'abcfed'
- reverse_suffix('abc', 3) == 'cba'
- reverse_suffix('abc', 0) == 'abc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0547 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_suffix(text: str, size: int) -> str:
    raise NotImplementedError("TODO: PB0547")


def self_test() -> None:
    assert reverse_suffix('abcdef', 3) == 'abcfed'
    assert reverse_suffix('abc', 3) == 'cba'
    assert reverse_suffix('abc', 0) == 'abc'
