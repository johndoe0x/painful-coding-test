"""
PB0702 — 기본값으로 조회

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
key가 있으면 해당 value, 없으면 default를 반환한다.

연습 초점
---------
dict.get 사용

구현할 함수
-----------
def dict_get_or_default(mapping: dict[str, int], key: str, default: int) -> int:

예시 및 필수 테스트
-------------------
- dict_get_or_default({'a': 1}, 'a', 9) == 1
- dict_get_or_default({'a': 1}, 'x', 9) == 9
- dict_get_or_default({}, '', 0) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0702 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_get_or_default(mapping: dict[str, int], key: str, default: int) -> int:
    raise NotImplementedError("TODO: PB0702")


def self_test() -> None:
    assert dict_get_or_default({'a': 1}, 'a', 9) == 1
    assert dict_get_or_default({'a': 1}, 'x', 9) == 9
    assert dict_get_or_default({}, '', 0) == 0
