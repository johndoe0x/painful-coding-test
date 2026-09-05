"""
PB0435 — 청크 시작 인덱스

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 chunk_size를 step으로 사용해 0부터 length 미만의 청크 시작 인덱스를 반환한다.

연습 초점
---------
자료 묶음 경계에 step 적용

구현할 함수
-----------
def chunk_start_indices(length: int, chunk_size: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- chunk_start_indices(10, 3) == [0, 3, 6, 9]
- chunk_start_indices(0, 4) == []
- chunk_start_indices(2, 5) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0435 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def chunk_start_indices(length: int, chunk_size: int) -> list[int]:
    raise NotImplementedError("TODO: PB0435")


def self_test() -> None:
    assert chunk_start_indices(10, 3) == [0, 3, 6, 9]
    assert chunk_start_indices(0, 4) == []
    assert chunk_start_indices(2, 5) == [0]
