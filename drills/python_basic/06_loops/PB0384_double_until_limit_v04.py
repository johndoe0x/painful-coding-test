"""
PB0384 — 한계까지 두 배

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 value를 while로 두 배씩 키워 limit 이상이 될 때까지 각 새 값을 반환하며 이미 이상이면 빈 리스트를 반환한다.

연습 초점
---------
변화하는 값 자체를 while 조건에 사용

구현할 함수
-----------
def double_until_limit(value: int, limit: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- double_until_limit(2, 10) == [4, 8, 16]
- double_until_limit(10, 10) == []
- double_until_limit(1, 2) == [2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0384 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def double_until_limit(value: int, limit: int) -> list[int]:
    raise NotImplementedError("TODO: PB0384")


def self_test() -> None:
    assert double_until_limit(2, 10) == [4, 8, 16]
    assert double_until_limit(10, 10) == []
    assert double_until_limit(1, 2) == [2]
