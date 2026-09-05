"""
PB0447 — 짝수 인덱스 값 역순

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
유효한 마지막 짝수 인덱스부터 0까지 step -2로 순회해 값을 반환한다.

연습 초점
---------
역방향 고정 step과 시작 인덱스 계산

구현할 함수
-----------
def even_index_values_reverse(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- even_index_values_reverse([10, 11, 12, 13, 14]) == [14, 12, 10]
- even_index_values_reverse([]) == []
- even_index_values_reverse([5, 6]) == [5]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0447 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def even_index_values_reverse(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0447")


def self_test() -> None:
    assert even_index_values_reverse([10, 11, 12, 13, 14]) == [14, 12, 10]
    assert even_index_values_reverse([]) == []
    assert even_index_values_reverse([5, 6]) == [5]
