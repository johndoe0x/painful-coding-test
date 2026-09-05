"""
PB0673 — 요청 권한 포함 검사

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
requested의 모든 권한이 granted에 포함되면 True를 반환한다.

연습 초점
---------
부분집합 비교

구현할 함수
-----------
def set_is_subset(requested: set[str], granted: set[str]) -> bool:

예시 및 필수 테스트
-------------------
- set_is_subset({'read'}, {'read', 'write'}) is True
- set_is_subset({'delete'}, {'read'}) is False
- set_is_subset(set(), {'read'}) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0673 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_is_subset(requested: set[str], granted: set[str]) -> bool:
    raise NotImplementedError("TODO: PB0673")


def self_test() -> None:
    assert set_is_subset({'read'}, {'read', 'write'}) is True
    assert set_is_subset({'delete'}, {'read'}) is False
    assert set_is_subset(set(), {'read'}) is True
