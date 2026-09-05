"""
PB0018 — 언어 정보 갱신

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
기본 정보 language='Python', typing='dynamic'에 extra를 덮어쓴 새 딕셔너리를 반환하세요.

연습 초점
---------
기본 딕셔너리와 갱신 데이터 병합

구현할 함수
-----------
def merge_python_info(extra: dict[str, str]) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- merge_python_info({'version': '3'}) == {'language': 'Python', 'typing': 'dynamic', 'version': '3'}
- merge_python_info({}) == {'language': 'Python', 'typing': 'dynamic'}
- merge_python_info({'typing': 'gradual'}) == {'language': 'Python', 'typing': 'gradual'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0018 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def merge_python_info(extra: dict[str, str]) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0018")


def self_test() -> None:
    assert merge_python_info({'version': '3'}) == {'language': 'Python', 'typing': 'dynamic', 'version': '3'}
    assert merge_python_info({}) == {'language': 'Python', 'typing': 'dynamic'}
    assert merge_python_info({'typing': 'gradual'}) == {'language': 'Python', 'typing': 'gradual'}
