"""
PB0572 — 두 값을 리스트로 바꾸기

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 원소 tuple의 값을 같은 순서의 새 리스트로 반환한다.

연습 초점
---------
tuple과 list의 표기 및 변환 결과 차이를 확인한다.

구현할 함수
-----------
def pair_as_list(pair: tuple[object, object]) -> list[object]:

예시 및 필수 테스트
-------------------
- pair_as_list(('a', 1)) == ['a', 1]
- pair_as_list((True, None)) == [True, None]
- pair_as_list(([], {})) == [[], {}]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0572 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pair_as_list(pair: tuple[object, object]) -> list[object]:
    raise NotImplementedError("TODO: PB0572")


def self_test() -> None:
    assert pair_as_list(('a', 1)) == ['a', 1]
    assert pair_as_list((True, None)) == [True, None]
    assert pair_as_list(([], {})) == [[], {}]
