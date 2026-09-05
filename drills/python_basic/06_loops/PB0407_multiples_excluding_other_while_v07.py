"""
PB0407 — 특정 배수 제외

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 base의 limit 이하 배수 중 양수 excluded의 배수는 제외해 while로 반환한다.

연습 초점
---------
배수 생성 중 추가 나머지 조건

구현할 함수
-----------
def multiples_excluding_other_while(limit: int, base: int, excluded: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- multiples_excluding_other_while(12, 3, 2) == [3, 9]
- multiples_excluding_other_while(5, 6, 2) == []
- multiples_excluding_other_while(10, 2, 5) == [2, 4, 6, 8]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0407 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def multiples_excluding_other_while(limit: int, base: int, excluded: int) -> list[int]:
    raise NotImplementedError("TODO: PB0407")


def self_test() -> None:
    assert multiples_excluding_other_while(12, 3, 2) == [3, 9]
    assert multiples_excluding_other_while(5, 6, 2) == []
    assert multiples_excluding_other_while(10, 2, 5) == [2, 4, 6, 8]
