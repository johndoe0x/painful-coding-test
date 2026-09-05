"""
PB0353 — 연령대 분류

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
13 미만 child, 20 미만 teen, 65 미만 adult, 그 이상 senior를 반환한다.

연습 초점
---------
여러 상한 경계를 순서대로 검사

구현할 함수
-----------
def age_group(age: int) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- age_group(12) == 'child'
- age_group(19) == 'teen'
- age_group(65) == 'senior'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0353 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def age_group(age: int) -> str:
    raise NotImplementedError("TODO: PB0353")


def self_test() -> None:
    assert age_group(12) == 'child'
    assert age_group(19) == 'teen'
    assert age_group(65) == 'senior'
