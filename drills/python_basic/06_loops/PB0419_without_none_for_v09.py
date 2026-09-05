"""
PB0419 — for None 제외

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 순회해 None이 아닌 정수만 원래 순서로 반환한다.

연습 초점
---------
선택적 타입 원소 필터링

구현할 함수
-----------
def without_none_for(values: list[int | None]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- without_none_for([1, None, 2]) == [1, 2]
- without_none_for([]) == []
- without_none_for([None, None]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0419 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def without_none_for(values: list[int | None]) -> list[int]:
    raise NotImplementedError("TODO: PB0419")


def self_test() -> None:
    assert without_none_for([1, None, 2]) == [1, 2]
    assert without_none_for([]) == []
    assert without_none_for([None, None]) == []
