"""
PB0795 — 누락 key 기본값

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: try

문제
----
대괄호로 key를 조회하고 KeyError가 발생하면 default를 반환한다.

연습 초점
---------
KeyError 포착

구현할 함수
-----------
def exc_lookup_or_default(mapping: dict[str, int], key: str, default: int) -> int:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_lookup_or_default({'a': 1}, 'a', 9) == 1
- exc_lookup_or_default({'a': 1}, 'x', 9) == 9
- exc_lookup_or_default({}, '', 0) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0795 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_lookup_or_default(mapping: dict[str, int], key: str, default: int) -> int:
    raise NotImplementedError("TODO: PB0795")


def self_test() -> None:
    assert exc_lookup_or_default({'a': 1}, 'a', 9) == 1
    assert exc_lookup_or_default({'a': 1}, 'x', 9) == 9
    assert exc_lookup_or_default({}, '', 0) == 0
