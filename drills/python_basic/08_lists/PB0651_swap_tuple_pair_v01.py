"""
PB0651 — tuple 두 원소 맞바꾸기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 원소 tuple을 언패킹해 순서를 바꾼 새 tuple을 반환한다.

연습 초점
---------
고정 길이 tuple 언패킹과 tuple 반환을 연습한다.

구현할 함수
-----------
def swap_pair(pair: tuple[object, object]) -> tuple[object, object]:

예시 및 필수 테스트
-------------------
- swap_pair(('a', 1)) == (1, 'a')
- swap_pair((True, None)) == (None, True)
- swap_pair(((1, 2), 'x')) == ('x', (1, 2))

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0651 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def swap_pair(pair: tuple[object, object]) -> tuple[object, object]:
    raise NotImplementedError("TODO: PB0651")


def self_test() -> None:
    assert swap_pair(('a', 1)) == (1, 'a')
    assert swap_pair((True, None)) == (None, True)
    assert swap_pair(((1, 2), 'x')) == ('x', (1, 2))
