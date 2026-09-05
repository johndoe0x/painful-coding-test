"""
PB0108 — 양끝과 중간 분리

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
길이 2 이상인 values를 first, *middle, last로 언패킹해 반환하세요.

연습 초점
---------
확장 다중 할당의 중간 수집

구현할 함수
-----------
def unpack_ends(values: list[str]) -> tuple[str, list[str], str]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- unpack_ends(['a', 'b', 'c']) == ('a', ['b'], 'c')
- unpack_ends(['a', 'b']) == ('a', [], 'b')
- unpack_ends(['', '']) == ('', [], '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0108 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unpack_ends(values: list[str]) -> tuple[str, list[str], str]:
    raise NotImplementedError("TODO: PB0108")


def self_test() -> None:
    assert unpack_ends(['a', 'b', 'c']) == ('a', ['b'], 'c')
    assert unpack_ends(['a', 'b']) == ('a', [], 'b')
    assert unpack_ends(['', '']) == ('', [], '')
