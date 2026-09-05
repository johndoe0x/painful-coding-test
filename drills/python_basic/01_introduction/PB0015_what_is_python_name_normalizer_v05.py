"""
PB0015 — Python 표기 통일

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
앞뒤 공백을 제거한 text가 대소문자와 무관하게 python이면 'Python', 아니면 정리된 원문을 반환하세요.

연습 초점
---------
표준 표기로 정규화

구현할 함수
-----------
def normalize_python_name(text: str) -> str:

예시 및 필수 테스트
-------------------
- normalize_python_name(' python ') == 'Python'
- normalize_python_name('') == ''
- normalize_python_name('Java') == 'Java'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0015 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def normalize_python_name(text: str) -> str:
    raise NotImplementedError("TODO: PB0015")


def self_test() -> None:
    assert normalize_python_name(' python ') == 'Python'
    assert normalize_python_name('') == ''
    assert normalize_python_name('Java') == 'Java'
