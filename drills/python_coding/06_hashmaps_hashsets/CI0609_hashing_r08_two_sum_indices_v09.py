"""
CI0609 — 두 수 합 index — 반복 세트 8

Chapter: Hashmaps and Hashsets
Seed: 31 / 40
Variant: 09 / 20
Time cap: 240 seconds
Source checks:

문제
----
한 번의 순회와 hashmap으로 합이 target인 0-based (i, j), i < j를 반환하세요. j가 가장 작은 쌍을 고르고 j가 같으면 i가 가장 작은 쌍을 선택합니다. 없으면 None입니다. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 8이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
complement lookup과 첫 index 보존

구현할 함수
-----------
def hashing_r08_two_sum_indices(values: list[int], target: int) -> tuple[int, int] | None:

예시 및 필수 테스트
-------------------
- hashing_r08_two_sum_indices([2, 7, 11, 15], 9) == (0, 1)
- (hashing_r08_two_sum_indices([3, 3], 6), hashing_r08_two_sum_indices([1, 1, 4], 5)) == ((0, 1), (0, 2))
- hashing_r08_two_sum_indices([1, 2], 9) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0609 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r08_two_sum_indices(values: list[int], target: int) -> tuple[int, int] | None:
    raise NotImplementedError("TODO: CI0609")


def self_test() -> None:
    assert hashing_r08_two_sum_indices([2, 7, 11, 15], 9) == (0, 1)
    assert (hashing_r08_two_sum_indices([3, 3], 6), hashing_r08_two_sum_indices([1, 1, 4], 5)) == ((0, 1), (0, 2))
    assert hashing_r08_two_sum_indices([1, 2], 9) is None
