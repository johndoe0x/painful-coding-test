"""
PB0294 — 전역 한도와 지역 한도

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
value가 GLOBAL_VALUE_LIMIT 이하인지와 local_limit 이하인지를 각각 계산해 tuple로 반환한다.

연습 초점
---------
전역 정책 경계와 지역 호출 경계의 독립 비교

구현할 함수
-----------
def within_global_and_local_limit(value: int, local_limit: int) -> tuple[bool, bool]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- within_global_and_local_limit(40, 30) == (True, False)
- within_global_and_local_limit(50, 50) == (True, True)
- within_global_and_local_limit(60, 100) == (False, True)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0294 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_VALUE_LIMIT = 50


def within_global_and_local_limit(value: int, local_limit: int) -> tuple[bool, bool]:
    raise NotImplementedError("TODO: PB0294")


def self_test() -> None:
    assert within_global_and_local_limit(40, 30) == (True, False)
    assert within_global_and_local_limit(50, 50) == (True, True)
    assert within_global_and_local_limit(60, 100) == (False, True)
