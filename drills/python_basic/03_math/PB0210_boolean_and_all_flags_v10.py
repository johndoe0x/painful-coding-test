"""
PB0210 — 모든 플래그 확인

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
flags가 비어 있지 않고 모든 값이 True이면 True를 반환하세요.

연습 초점
---------
비어 있지 않음과 all 결과 결합

구현할 함수
-----------
def all_flags_enabled(flags: list[bool]) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- all_flags_enabled([True, True]) is True
- all_flags_enabled([]) is False
- all_flags_enabled([True, False]) is False and all_flags_enabled([False, True]) is False and all_flags_enabled([False]) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0210 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def all_flags_enabled(flags: list[bool]) -> bool:
    raise NotImplementedError("TODO: PB0210")


def self_test() -> None:
    assert all_flags_enabled([True, True]) is True
    assert all_flags_enabled([]) is False
    assert all_flags_enabled([True, False]) is False and all_flags_enabled([False, True]) is False and all_flags_enabled([False]) is False
