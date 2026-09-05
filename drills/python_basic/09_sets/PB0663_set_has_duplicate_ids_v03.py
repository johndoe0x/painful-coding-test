"""
PB0663 — 중복 ID 감지

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 ID가 두 번 이상 등장하면 True를 반환한다.

연습 초점
---------
원본 길이와 set 길이 비교

구현할 함수
-----------
def set_has_duplicate_ids(ids: list[str]) -> bool:

예시 및 필수 테스트
-------------------
- set_has_duplicate_ids(['a', 'b', 'a']) is True
- set_has_duplicate_ids(['a', 'b']) is False
- set_has_duplicate_ids([]) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0663 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_has_duplicate_ids(ids: list[str]) -> bool:
    raise NotImplementedError("TODO: PB0663")


def self_test() -> None:
    assert set_has_duplicate_ids(['a', 'b', 'a']) is True
    assert set_has_duplicate_ids(['a', 'b']) is False
    assert set_has_duplicate_ids([]) is False
