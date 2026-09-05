"""
CI0169 — JSON 객체 파싱 — 반복 세트 4

Chapter: Pythonic Code
Seed: 09 / 40
Variant: 09 / 20
Time cap: 240 seconds
Source checks: json_call

문제
----
json.loads로 JSON object를 파싱하고 정렬된 keys, key 개수, 원본 data를 딕셔너리로 반환하세요. 이 파일은 Pythonic Code 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
JSON 역직렬화와 구조 확인

구현할 함수
-----------
def pythonic_r04_json_object_summary(text: str) -> dict[str, object]:

필수 구현 방식
--------------
- json API를 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_r04_json_object_summary('{"b": 2, "a": 1}') == {'keys': ['a', 'b'], 'count': 2, 'data': {'b': 2, 'a': 1}}
- pythonic_r04_json_object_summary('{}') == {'keys': [], 'count': 0, 'data': {}}
- pythonic_r04_json_object_summary('{"x": [1, 2]}') == {'keys': ['x'], 'count': 1, 'data': {'x': [1, 2]}}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0169 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r04_json_object_summary(text: str) -> dict[str, object]:
    raise NotImplementedError("TODO: CI0169")


def self_test() -> None:
    assert pythonic_r04_json_object_summary('{"b": 2, "a": 1}') == {'keys': ['a', 'b'], 'count': 2, 'data': {'b': 2, 'a': 1}}
    assert pythonic_r04_json_object_summary('{}') == {'keys': [], 'count': 0, 'data': {}}
    assert pythonic_r04_json_object_summary('{"x": [1, 2]}') == {'keys': ['x'], 'count': 1, 'data': {'x': [1, 2]}}
