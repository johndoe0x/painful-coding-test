"""
PB0413 — for 문자열 길이

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 각 문자열의 길이를 반환 리스트에 담는다.

연습 초점
---------
입력 원소와 다른 타입 결과 누적

구현할 함수
-----------
def lengths_all_for(words: list[str]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- lengths_all_for(['a', 'code']) == [1, 4]
- lengths_all_for([]) == []
- lengths_all_for(['', '한글']) == [0, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0413 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def lengths_all_for(words: list[str]) -> list[int]:
    raise NotImplementedError("TODO: PB0413")


def self_test() -> None:
    assert lengths_all_for(['a', 'code']) == [1, 4]
    assert lengths_all_for([]) == []
    assert lengths_all_for(['', '한글']) == [0, 2]
