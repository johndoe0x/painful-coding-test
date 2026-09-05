"""
PB0450 — 끝에서부터 청크

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 chunk_size에 대해 끝에서부터 최대 chunk_size개씩 묶되 각 묶음 내부 순서는 원래대로 반환한다.

연습 초점
---------
역순 경계 이동과 슬라이스

구현할 함수
-----------
def chunks_from_end(values: list[int], chunk_size: int) -> list[list[int]]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- chunks_from_end([1, 2, 3, 4, 5], 2) == [[4, 5], [2, 3], [1]]
- chunks_from_end([], 3) == []
- chunks_from_end([1, 2], 5) == [[1, 2]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0450 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def chunks_from_end(values: list[int], chunk_size: int) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0450")


def self_test() -> None:
    assert chunks_from_end([1, 2, 3, 4, 5], 2) == [[4, 5], [2, 3], [1]]
    assert chunks_from_end([], 3) == []
    assert chunks_from_end([1, 2], 5) == [[1, 2]]
