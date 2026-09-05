"""
PB0797 — 전체 정수 변환 또는 빈 목록

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: try

문제
----
모든 문자열을 int로 변환한다. 하나라도 ValueError가 나면 부분 결과를 버리고 빈 리스트를 반환한다.

연습 초점
---------
list comprehension 전체를 감싸는 try-except

구현할 함수
-----------
def exc_convert_all_or_empty(texts: list[str]) -> list[int]:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_convert_all_or_empty(['1', '2']) == [1, 2]
- exc_convert_all_or_empty(['1', 'x', '2']) == []
- exc_convert_all_or_empty([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0797 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_convert_all_or_empty(texts: list[str]) -> list[int]:
    raise NotImplementedError("TODO: PB0797")


def self_test() -> None:
    assert exc_convert_all_or_empty(['1', '2']) == [1, 2]
    assert exc_convert_all_or_empty(['1', 'x', '2']) == []
    assert exc_convert_all_or_empty([]) == []
