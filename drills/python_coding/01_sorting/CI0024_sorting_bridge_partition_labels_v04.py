"""
CI0024 — 정렬 사고 → 문자 구간 분할

Chapter: Sorting
Seed: 02 / 40
Variant: 04 / 20
Time cap: 420 seconds
Source checks:

문제
----
길이 0~500의 소문자 영문 문자열을 같은 문자가 둘 이상의 조각에 나타나지 않도록 최대한 많은 연속 조각으로 나누세요. 조각 길이를 원래 순서대로 반환하며 빈 문자열은 []입니다.

연습 초점
---------
마지막 출현 위치와 구간 경계 그리디

구현할 함수
-----------
def sorting_bridge_partition_labels(text: str) -> list[int]:

예시 및 필수 테스트
-------------------
- sorting_bridge_partition_labels('') == [] and sorting_bridge_partition_labels('abc') == [1, 1, 1]
- sorting_bridge_partition_labels('ababcbacadefegdehijhklij') == [9, 7, 8]
- sorting_bridge_partition_labels('abac') == [3, 1] and sorting_bridge_partition_labels('aaaa') == [4]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0024 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_bridge_partition_labels(text: str) -> list[int]:
    raise NotImplementedError("TODO: CI0024")


def self_test() -> None:
    assert sorting_bridge_partition_labels('') == [] and sorting_bridge_partition_labels('abc') == [1, 1, 1]
    assert sorting_bridge_partition_labels('ababcbacadefegdehijhklij') == [9, 7, 8]
    assert sorting_bridge_partition_labels('abac') == [3, 1] and sorting_bridge_partition_labels('aaaa') == [4]
