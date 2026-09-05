"""
PB0401 — 한계 이하 배수

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 base의 배수를 base부터 limit 이하까지 while로 만들어 반환한다.

연습 초점
---------
배수만큼 증가하는 while

구현할 함수
-----------
def multiples(limit: int, base: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- multiples(10, 3) == [3, 6, 9]
- multiples(2, 3) == []
- multiples(6, 2) == [2, 4, 6]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0401 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def multiples(limit: int, base: int) -> list[int]:
    raise NotImplementedError("TODO: PB0401")


def self_test() -> None:
    assert multiples(10, 3) == [3, 6, 9]
    assert multiples(2, 3) == []
    assert multiples(6, 2) == [2, 4, 6]
