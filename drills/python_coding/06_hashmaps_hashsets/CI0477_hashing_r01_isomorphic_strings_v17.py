"""
CI0477 — 동형 문자열 — 반복 세트 1

Chapter: Hashmaps and Hashsets
Seed: 24 / 40
Variant: 17 / 20
Time cap: 240 seconds
Source checks:

문제
----
문자열 길이가 같고 각 위치의 문자 대응이 양방향 일대일이면 True를 반환하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
bijection hash maps와 길이 검증

구현할 함수
-----------
def hashing_r01_isomorphic_strings(left: str, right: str) -> bool:

예시 및 필수 테스트
-------------------
- hashing_r01_isomorphic_strings('egg', 'add') is True
- (hashing_r01_isomorphic_strings('foo', 'bar'), hashing_r01_isomorphic_strings('ab', 'aa'), hashing_r01_isomorphic_strings('ab', 'abc')) == (False, False, False)
- hashing_r01_isomorphic_strings('', '') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0477 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r01_isomorphic_strings(left: str, right: str) -> bool:
    raise NotImplementedError("TODO: CI0477")


def self_test() -> None:
    assert hashing_r01_isomorphic_strings('egg', 'add') is True
    assert (hashing_r01_isomorphic_strings('foo', 'bar'), hashing_r01_isomorphic_strings('ab', 'aa'), hashing_r01_isomorphic_strings('ab', 'abc')) == (False, False, False)
    assert hashing_r01_isomorphic_strings('', '') is True
