"""
PB0158 — 선택적 프로필 이름

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
profile이 None이거나 name 키가 없으면 'anonymous', 아니면 name 값을 반환하세요. 빈 name은 그대로 반환하세요.

연습 초점
---------
None·누락 키·빈 값 구분

구현할 함수
-----------
def optional_profile_name(profile: dict[str, str] | None) -> str:

예시 및 필수 테스트
-------------------
- optional_profile_name({'name': 'Ada'}) == 'Ada'
- optional_profile_name(None) == 'anonymous'
- optional_profile_name({'name': ''}) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0158 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_profile_name(profile: dict[str, str] | None) -> str:
    raise NotImplementedError("TODO: PB0158")


def self_test() -> None:
    assert optional_profile_name({'name': 'Ada'}) == 'Ada'
    assert optional_profile_name(None) == 'anonymous'
    assert optional_profile_name({'name': ''}) == ''
