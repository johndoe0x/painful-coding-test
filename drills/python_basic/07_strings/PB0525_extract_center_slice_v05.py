"""
PB0525 — 가운데 구간 자르기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
size가 text 길이 이하이고 둘의 홀짝이 같다고 가정해, 정확히 size글자인 가운데 부분을 반환한다.

연습 초점
---------
전체 길이와 목표 길이 차이로 대칭 슬라이스 경계를 계산한다.

구현할 함수
-----------
def center_slice(text: str, size: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- center_slice('abcdefgh', 4) == 'cdef'
- center_slice('abcde', 3) == 'bcd'
- center_slice('abc', 0) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0525 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def center_slice(text: str, size: int) -> str:
    raise NotImplementedError("TODO: PB0525")


def self_test() -> None:
    assert center_slice('abcdefgh', 4) == 'cdef'
    assert center_slice('abcde', 3) == 'bcd'
    assert center_slice('abc', 0) == ''
