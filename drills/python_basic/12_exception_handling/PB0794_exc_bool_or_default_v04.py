"""
PB0794 — 엄격한 bool 변환

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: try

문제
----
대소문자를 무시해 true/false만 허용한다. 그 밖의 값은 ValueError를 발생시킨 뒤 except에서 default를 반환한다.

연습 초점
---------
직접 raise한 ValueError 처리

구현할 함수
-----------
def exc_bool_or_default(text: str, default: bool) -> bool:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_bool_or_default('TRUE', False) is True
- exc_bool_or_default('false', True) is False
- exc_bool_or_default('yes', True) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0794 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_bool_or_default(text: str, default: bool) -> bool:
    raise NotImplementedError("TODO: PB0794")


def self_test() -> None:
    assert exc_bool_or_default('TRUE', False) is True
    assert exc_bool_or_default('false', True) is False
    assert exc_bool_or_default('yes', True) is True
