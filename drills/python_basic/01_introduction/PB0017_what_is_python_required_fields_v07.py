"""
PB0017 — 필수 정보 검사

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
info에 language='Python'과 typing='dynamic'이 모두 정확히 있으면 True를 반환하세요.

연습 초점
---------
딕셔너리 필드 조회와 동시 조건

구현할 함수
-----------
def has_python_fields(info: dict[str, str]) -> bool:

예시 및 필수 테스트
-------------------
- has_python_fields({'language': 'Python', 'typing': 'dynamic'}) is True
- has_python_fields({}) is False
- has_python_fields({'language': 'Python', 'typing': 'static'}) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0017 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_python_fields(info: dict[str, str]) -> bool:
    raise NotImplementedError("TODO: PB0017")


def self_test() -> None:
    assert has_python_fields({'language': 'Python', 'typing': 'dynamic'}) is True
    assert has_python_fields({}) is False
    assert has_python_fields({'language': 'Python', 'typing': 'static'}) is False
