"""
PB0429 — 인덱스 구간 복사

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(values)이고 stop >= 0이라고 가정합니다. for와 range(start, min(stop, len(values)))로 지정 구간의 원소를 새 리스트에 복사하며 stop <= start이면 []를 반환한다.

연습 초점
---------
유효한 start·stop이 있는 인덱스 range

구현할 함수
-----------
def copy_index_window(values: list[int], start: int, stop: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- copy_index_window([1, 2, 3, 4], 1, 3) == [2, 3]
- copy_index_window([], 0, 2) == []
- copy_index_window([1, 2], 1, 9) == [2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0429 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def copy_index_window(values: list[int], start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0429")


def self_test() -> None:
    assert copy_index_window([1, 2, 3, 4], 1, 3) == [2, 3]
    assert copy_index_window([], 0, 2) == []
    assert copy_index_window([1, 2], 1, 9) == [2]
