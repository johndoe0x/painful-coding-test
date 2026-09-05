"""
PB0796 — 범위 밖 인덱스 기본값

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: try

문제
----
values[index]를 반환하고 IndexError가 발생하면 default를 반환한다. Python의 음수 인덱스는 그대로 허용한다.

연습 초점
---------
IndexError와 유효한 음수 인덱스 구분

구현할 함수
-----------
def exc_index_or_default(values: list[object], index: int, default: object) -> object:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_index_or_default(['a'], 0, 'x') == 'a'
- exc_index_or_default(['a'], 2, 'x') == 'x'
- exc_index_or_default(['a', 'b'], -1, 'x') == 'b'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0796 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_index_or_default(values: list[object], index: int, default: object) -> object:
    raise NotImplementedError("TODO: PB0796")


def self_test() -> None:
    assert exc_index_or_default(['a'], 0, 'x') == 'a'
    assert exc_index_or_default(['a'], 2, 'x') == 'x'
    assert exc_index_or_default(['a', 'b'], -1, 'x') == 'b'
