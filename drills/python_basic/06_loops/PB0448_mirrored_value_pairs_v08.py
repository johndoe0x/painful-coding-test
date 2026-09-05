"""
PB0448 — 양끝 거울 쌍

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
정방향 인덱스와 대응하는 역순 인덱스의 값을 tuple로 묶어 모든 위치에 대해 반환한다.

연습 초점
---------
정방향과 역방향 인덱스 대응

구현할 함수
-----------
def mirrored_value_pairs(values: list[str]) -> list[tuple[str, str]]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- mirrored_value_pairs(['a', 'b', 'c']) == [('a', 'c'), ('b', 'b'), ('c', 'a')]
- mirrored_value_pairs([]) == []
- mirrored_value_pairs(['x']) == [('x', 'x')]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0448 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mirrored_value_pairs(values: list[str]) -> list[tuple[str, str]]:
    raise NotImplementedError("TODO: PB0448")


def self_test() -> None:
    assert mirrored_value_pairs(['a', 'b', 'c']) == [('a', 'c'), ('b', 'b'), ('c', 'a')]
    assert mirrored_value_pairs([]) == []
    assert mirrored_value_pairs(['x']) == [('x', 'x')]
