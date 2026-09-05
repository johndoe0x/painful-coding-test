"""
PB0489 — 이웃 글자 확인하기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
유효한 0 이상 인덱스 index의 바로 왼쪽과 오른쪽 글자를 반환하며 경계 밖 이웃은 None으로 표시한다.

연습 초점
---------
현재 인덱스 양옆의 경계를 각각 검사한다.

구현할 함수
-----------
def character_neighbors(text: str, index: int) -> tuple[str | None, str | None]:

예시 및 필수 테스트
-------------------
- character_neighbors('abcd', 1) == ('a', 'c')
- character_neighbors('abcd', 0) == (None, 'b')
- character_neighbors('abcd', 3) == ('c', None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0489 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def character_neighbors(text: str, index: int) -> tuple[str | None, str | None]:
    raise NotImplementedError("TODO: PB0489")


def self_test() -> None:
    assert character_neighbors('abcd', 1) == ('a', 'c')
    assert character_neighbors('abcd', 0) == (None, 'b')
    assert character_neighbors('abcd', 3) == ('c', None)
