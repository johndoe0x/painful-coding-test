"""
PB0378 — 설정 활성 상태

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: if

문제
----
value의 truthiness를 정확한 bool 값으로 변환해 반환한다.

연습 초점
---------
bool 변환으로 truthiness 확인

구현할 함수
-----------
def config_enabled_truthy(value: object) -> bool:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- config_enabled_truthy('yes') is True
- config_enabled_truthy({}) is False
- config_enabled_truthy(0) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0378 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def config_enabled_truthy(value: object) -> bool:
    raise NotImplementedError("TODO: PB0378")


def self_test() -> None:
    assert config_enabled_truthy('yes') is True
    assert config_enabled_truthy({}) is False
    assert config_enabled_truthy(0) is False
