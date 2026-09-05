"""
CI0423 — 2차원 표 → 편집 거리

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 03 / 20
Time cap: 900 seconds
Source checks:

문제
----
길이 0~100의 소문자 영문 문자열 left를 right로 바꾸는 최소 연산 수를 반환하세요. 문자 하나의 삽입·삭제·치환은 각각 비용 1이며 같은 문자 유지는 0입니다. 문자 순서를 교환하는 연산은 없습니다.

연습 초점
---------
문자열 접두사 쌍의 2차원 DP

구현할 함수
-----------
def grid_bridge_edit_distance(left: str, right: str) -> int:

예시 및 필수 테스트
-------------------
- grid_bridge_edit_distance('', '') == 0 and grid_bridge_edit_distance('', 'abc') == 3
- grid_bridge_edit_distance('horse', 'ros') == 3 and grid_bridge_edit_distance('ab', 'ba') == 2
- grid_bridge_edit_distance('kitten', 'sitting') == 3 and grid_bridge_edit_distance('same', 'same') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0423 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_bridge_edit_distance(left: str, right: str) -> int:
    raise NotImplementedError("TODO: CI0423")


def self_test() -> None:
    assert grid_bridge_edit_distance('', '') == 0 and grid_bridge_edit_distance('', 'abc') == 3
    assert grid_bridge_edit_distance('horse', 'ros') == 3 and grid_bridge_edit_distance('ab', 'ba') == 2
    assert grid_bridge_edit_distance('kitten', 'sitting') == 3 and grid_bridge_edit_distance('same', 'same') == 0
