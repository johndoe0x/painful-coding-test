"""
PB0272 — 선택적 이름 목록 라벨

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
None은 '(missing)', 빈 문자열은 '(empty)', 그 외 문자열은 'user:<name>'으로 바꿔 원래 순서의 리스트를 반환한다. 공백은 제거하지 않는다.

연습 초점
---------
중첩 컬렉션의 union 타입과 None·빈 문자열의 구별

구현할 함수
-----------
def label_optional_names(names: list[str | None]) -> list[str]:

예시 및 필수 테스트
-------------------
- label_optional_names(['Ada', None, '']) == ['user:Ada', '(missing)', '(empty)']
- label_optional_names([]) == []
- label_optional_names([' ', '0', None]) == ['user: ', 'user:0', '(missing)']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0272 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def label_optional_names(names: list[str | None]) -> list[str]:
    raise NotImplementedError("TODO: PB0272")


def self_test() -> None:
    assert label_optional_names(['Ada', None, '']) == ['user:Ada', '(missing)', '(empty)']
    assert label_optional_names([]) == []
    assert label_optional_names([' ', '0', None]) == ['user: ', 'user:0', '(missing)']
