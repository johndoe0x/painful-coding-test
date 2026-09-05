"""
PB0342 — 성인 여부 구분

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
age가 18 이상이면 'adult', 아니면 'minor'를 반환한다.

연습 초점
---------
경계값을 양쪽 분기로 나누기

구현할 함수
-----------
def adult_or_minor(age: int) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- adult_or_minor(18) == 'adult'
- adult_or_minor(17) == 'minor'
- adult_or_minor(0) == 'minor'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0342 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def adult_or_minor(age: int) -> str:
    raise NotImplementedError("TODO: PB0342")


def self_test() -> None:
    assert adult_or_minor(18) == 'adult'
    assert adult_or_minor(17) == 'minor'
    assert adult_or_minor(0) == 'minor'
