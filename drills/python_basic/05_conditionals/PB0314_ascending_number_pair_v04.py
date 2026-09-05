"""
PB0314 — 오름차순 숫자 쌍

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 수를 비교해 작은 값이 앞에 오도록 반환한다.

연습 초점
---------
<= 비교로 동률까지 처리

구현할 함수
-----------
def ascending_number_pair(a: int, b: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- ascending_number_pair(8, 3) == (3, 8)
- ascending_number_pair(4, 4) == (4, 4)
- ascending_number_pair(-1, -5) == (-5, -1)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0314 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def ascending_number_pair(a: int, b: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0314")


def self_test() -> None:
    assert ascending_number_pair(8, 3) == (3, 8)
    assert ascending_number_pair(4, 4) == (4, 4)
    assert ascending_number_pair(-1, -5) == (-5, -1)
