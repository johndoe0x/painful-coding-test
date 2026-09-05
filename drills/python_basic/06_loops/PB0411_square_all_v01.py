"""
PB0411 — for 전체 제곱

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 각 숫자의 제곱을 같은 순서의 새 리스트에 담는다.

연습 초점
---------
컬렉션 원소 직접 순회

구현할 함수
-----------
def square_all(numbers: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- square_all([1, 3]) == [1, 9]
- square_all([]) == []
- square_all([-2, 0]) == [4, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0411 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def square_all(numbers: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0411")


def self_test() -> None:
    assert square_all([1, 3]) == [1, 9]
    assert square_all([]) == []
    assert square_all([-2, 0]) == [4, 0]
