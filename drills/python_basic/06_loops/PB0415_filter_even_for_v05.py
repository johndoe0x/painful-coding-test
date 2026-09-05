"""
PB0415 — for 짝수 필터

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 순회해 짝수만 원래 순서로 반환한다.

연습 초점
---------
조건에 맞는 원소만 append

구현할 함수
-----------
def filter_even_for(numbers: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- filter_even_for([1, 2, 4, 5]) == [2, 4]
- filter_even_for([]) == []
- filter_even_for([-3, -2, 0]) == [-2, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0415 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def filter_even_for(numbers: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0415")


def self_test() -> None:
    assert filter_even_for([1, 2, 4, 5]) == [2, 4]
    assert filter_even_for([]) == []
    assert filter_even_for([-3, -2, 0]) == [-2, 0]
