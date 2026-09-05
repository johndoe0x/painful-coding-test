"""
CI0125 — zip으로 두 열을 딕셔너리로

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 05 / 20
Time cap: 150 seconds
Source checks: zip_call

문제
----
dict(zip(keys, values))로 딕셔너리를 만드세요. 짧은 열 길이까지만 사용하고 같은 key는 마지막 값을 남깁니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
zip 길이와 dict 중복 키

구현할 함수
-----------
def pythonic_fluency_zip_to_mapping(keys: list[str], values: list[int]) -> dict[str, int]:

필수 구현 방식
--------------
- zip()을 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_fluency_zip_to_mapping(['a', 'b', 'a'], [1, 2, 3]) == {'a': 3, 'b': 2}
- pythonic_fluency_zip_to_mapping([], [1]) == {}
- ((_practice_1_0 := ['x', 'y']), (_practice_1_1 := [0]), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := pythonic_fluency_zip_to_mapping(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == {'x': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0125 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_fluency_zip_to_mapping(keys: list[str], values: list[int]) -> dict[str, int]:
    raise NotImplementedError("TODO: CI0125")


def self_test() -> None:
    assert pythonic_fluency_zip_to_mapping(['a', 'b', 'a'], [1, 2, 3]) == {'a': 3, 'b': 2}
    assert pythonic_fluency_zip_to_mapping([], [1]) == {}
    assert ((_practice_1_0 := ['x', 'y']), (_practice_1_1 := [0]), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := pythonic_fluency_zip_to_mapping(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == {'x': 0}
