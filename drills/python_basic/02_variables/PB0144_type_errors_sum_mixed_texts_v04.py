"""
PB0144 — 숫자 텍스트 목록 합계

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 문자열을 float로 변환해 전체 합을 반환하세요.

연습 초점
---------
같은 수치 타입으로 통일

구현할 함수
-----------
def sum_number_texts(values: list[str]) -> float:

예시 및 필수 테스트
-------------------
- sum_number_texts(['1.5', '2']) == 3.5
- sum_number_texts([]) == 0
- sum_number_texts(['-1', '1']) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0144 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_number_texts(values: list[str]) -> float:
    raise NotImplementedError("TODO: PB0144")


def self_test() -> None:
    assert sum_number_texts(['1.5', '2']) == 3.5
    assert sum_number_texts([]) == 0
    assert sum_number_texts(['-1', '1']) == 0.0
