"""
PB0578 — 두 개의 안쪽 리스트 만들기

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
[a, b]와 [c, d]를 각각 안쪽 리스트로 만들어 바깥 리스트에 담는다.

연습 초점
---------
중첩 리스트 리터럴의 계층과 원소 순서를 익힌다.

구현할 함수
-----------
def nested_pairs(a: object, b: object, c: object, d: object) -> list[list[object]]:

예시 및 필수 테스트
-------------------
- nested_pairs(1, 2, 3, 4) == [[1, 2], [3, 4]]
- nested_pairs('a', True, None, 0) == [['a', True], [None, 0]]
- nested_pairs([], {}, (), '') == [[[], {}], [(), '']]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0578 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def nested_pairs(a: object, b: object, c: object, d: object) -> list[list[object]]:
    raise NotImplementedError("TODO: PB0578")


def self_test() -> None:
    assert nested_pairs(1, 2, 3, 4) == [[1, 2], [3, 4]]
    assert nested_pairs('a', True, None, 0) == [['a', True], [None, 0]]
    assert nested_pairs([], {}, (), '') == [[[], {}], [(), '']]
