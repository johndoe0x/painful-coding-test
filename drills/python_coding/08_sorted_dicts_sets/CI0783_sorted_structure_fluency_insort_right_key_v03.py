"""
CI0783 — key가 있는 insort_right

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 03 / 20
Time cap: 240 seconds
Source checks: bisect_call, lambda

문제
----
records는 첫 정수 필드 오름차순입니다. 사본에 bisect.insort_right(..., key=lambda item: item[0])로 incoming을 삽입하세요. 같은 key 그룹 뒤에 삽입하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
insort의 key와 동률 오른쪽 삽입

구현할 함수
-----------
def sorted_structure_fluency_insort_right_key(records: list[tuple[int, str]], incoming: tuple[int, str]) -> list[tuple[int, str]]:

필수 구현 방식
--------------
- bisect API를 사용한다.
- lambda 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_fluency_insort_right_key([(1, 'b'), (1, 'a'), (3, 'x')], (1, 'z')) == [(1, 'b'), (1, 'a'), (1, 'z'), (3, 'x')]
- sorted_structure_fluency_insort_right_key([], (0, 'a')) == [(0, 'a')]
- ((_practice_1_0 := [(2, 'x')]), (_practice_1_1 := (1, 'y')), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_insort_right_key(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [(1, 'y'), (2, 'x')]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0783 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_fluency_insort_right_key(records: list[tuple[int, str]], incoming: tuple[int, str]) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: CI0783")


def self_test() -> None:
    assert sorted_structure_fluency_insort_right_key([(1, 'b'), (1, 'a'), (3, 'x')], (1, 'z')) == [(1, 'b'), (1, 'a'), (1, 'z'), (3, 'x')]
    assert sorted_structure_fluency_insort_right_key([], (0, 'a')) == [(0, 'a')]
    assert ((_practice_1_0 := [(2, 'x')]), (_practice_1_1 := (1, 'y')), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_insort_right_key(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [(1, 'y'), (2, 'x')]
