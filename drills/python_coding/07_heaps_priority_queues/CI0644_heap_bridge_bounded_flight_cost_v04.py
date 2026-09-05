"""
CI0644 — 우선순위 → 경유 횟수 제한 최단 비용

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 04 / 20
Time cap: 900 seconds
Source checks:

문제
----
1<=n<=50 정점, 최대 300개 유향 항공편 (u,v,비용 0~1000), 유효 source/target, 0<=stops<=20입니다. 최대 stops번 중간 경유, 즉 최대 stops+1개 간선을 이용한 최소 비용을 반환하세요. 도달 불가면 -1, source=target이면 0입니다. 중복/자기 간선 허용, 입력은 보존합니다.

연습 초점
---------
비용만이 아닌 남은 간선 수를 포함하는 상태

구현할 함수
-----------
def heap_bridge_bounded_flight_cost(n: int, flights: list[tuple[int, int, int]], source: int, target: int, stops: int) -> int:

예시 및 필수 테스트
-------------------
- heap_bridge_bounded_flight_cost(1, [], 0, 0, 0) == 0 and heap_bridge_bounded_flight_cost(2, [], 0, 1, 3) == -1
- heap_bridge_bounded_flight_cost(3, [(0, 1, 1), (1, 2, 1), (0, 2, 9)], 0, 2, 0) == 9
- ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1, 1), (1, 2, 1), (0, 2, 9)]), (_bridge_1_arg_2 := 0), (_bridge_1_arg_3 := 2), (_bridge_1_arg_4 := 1), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_bounded_flight_cost(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2, _bridge_1_arg_3, _bridge_1_arg_4)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0644 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_bridge_bounded_flight_cost(n: int, flights: list[tuple[int, int, int]], source: int, target: int, stops: int) -> int:
    raise NotImplementedError("TODO: CI0644")


def self_test() -> None:
    assert heap_bridge_bounded_flight_cost(1, [], 0, 0, 0) == 0 and heap_bridge_bounded_flight_cost(2, [], 0, 1, 3) == -1
    assert heap_bridge_bounded_flight_cost(3, [(0, 1, 1), (1, 2, 1), (0, 2, 9)], 0, 2, 0) == 9
    assert ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1, 1), (1, 2, 1), (0, 2, 9)]), (_bridge_1_arg_2 := 0), (_bridge_1_arg_3 := 2), (_bridge_1_arg_4 := 1), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_bounded_flight_cost(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2, _bridge_1_arg_3, _bridge_1_arg_4)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] == 2
