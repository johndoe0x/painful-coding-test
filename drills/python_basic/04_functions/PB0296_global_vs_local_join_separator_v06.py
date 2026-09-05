"""
PB0296 — 전역 구분자와 지역 구분자

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
parts를 GLOBAL_JOIN_SEPARATOR와 local_separator로 각각 결합해 두 문자열을 반환한다.

연습 초점
---------
전역 서식 상수와 호출별 지역 서식 값 비교

구현할 함수
-----------
def join_with_global_and_local_separator(parts: list[str], local_separator: str) -> tuple[str, str]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- join_with_global_and_local_separator(['a', 'b'], '-') == ('a|b', 'a-b')
- join_with_global_and_local_separator([], ',') == ('', '')
- join_with_global_and_local_separator(['x'], '') == ('x', 'x')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0296 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_JOIN_SEPARATOR = '|'


def join_with_global_and_local_separator(parts: list[str], local_separator: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0296")


def self_test() -> None:
    assert join_with_global_and_local_separator(['a', 'b'], '-') == ('a|b', 'a-b')
    assert join_with_global_and_local_separator([], ',') == ('', '')
    assert join_with_global_and_local_separator(['x'], '') == ('x', 'x')
