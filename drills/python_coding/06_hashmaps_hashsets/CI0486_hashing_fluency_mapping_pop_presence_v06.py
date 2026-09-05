"""
CI0486 — dict.pop 값과 키 존재 여부

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 06 / 20
Time cap: 180 seconds
Source checks: pop_call

문제
----
사본에서 pop(key, None)을 수행해 (호출 전 키 존재 여부, 꺼낸 값, 남은 사본)을 반환하세요. 저장된 None과 누락을 구별하고 원본은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
pop default와 존재 여부

구현할 함수
-----------
def hashing_fluency_mapping_pop_presence(mapping: dict[str, int | None], key: str) -> tuple[bool, int | None, dict[str, int | None]]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- hashing_fluency_mapping_pop_presence({'a': None, 'b': 2}, 'a') == (True, None, {'b': 2})
- hashing_fluency_mapping_pop_presence({}, 'x') == (False, None, {})
- ((_practice_1_0 := {'a': 0}), (_practice_1_1 := 'a'), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := hashing_fluency_mapping_pop_presence(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (True, 0, {})

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0486 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_fluency_mapping_pop_presence(mapping: dict[str, int | None], key: str) -> tuple[bool, int | None, dict[str, int | None]]:
    raise NotImplementedError("TODO: CI0486")


def self_test() -> None:
    assert hashing_fluency_mapping_pop_presence({'a': None, 'b': 2}, 'a') == (True, None, {'b': 2})
    assert hashing_fluency_mapping_pop_presence({}, 'x') == (False, None, {})
    assert ((_practice_1_0 := {'a': 0}), (_practice_1_1 := 'a'), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := hashing_fluency_mapping_pop_presence(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (True, 0, {})
