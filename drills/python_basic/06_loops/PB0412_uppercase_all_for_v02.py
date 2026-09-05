"""
PB0412 — for 전체 대문자

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 각 문자열을 대문자로 바꾼 새 리스트를 반환한다.

연습 초점
---------
문자열 리스트의 원소별 변환

구현할 함수
-----------
def uppercase_all_for(words: list[str]) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- uppercase_all_for(['Ada', 'py']) == ['ADA', 'PY']
- uppercase_all_for([]) == []
- uppercase_all_for(['']) == ['']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0412 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def uppercase_all_for(words: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0412")


def self_test() -> None:
    assert uppercase_all_for(['Ada', 'py']) == ['ADA', 'PY']
    assert uppercase_all_for([]) == []
    assert uppercase_all_for(['']) == ['']
