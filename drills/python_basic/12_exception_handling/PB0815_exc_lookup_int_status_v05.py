"""
PB0815 — 딕셔너리 문자열 숫자 조회

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
mapping[key]를 int로 바꾼다. KeyError면 missing, ValueError면 invalid, 성공하면 ok 상태를 반환한다.

연습 초점
---------
KeyError와 ValueError의 발생 순서 이해

구현할 함수
-----------
def exc_lookup_int_status(mapping: dict[str, str], key: str) -> tuple[str, int | None]:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_lookup_int_status({'a': '10'}, 'a') == ('ok', 10)
- exc_lookup_int_status({}, 'a') == ('missing', None)
- exc_lookup_int_status({'a': 'x'}, 'a') == ('invalid', None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0815 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_lookup_int_status(mapping: dict[str, str], key: str) -> tuple[str, int | None]:
    raise NotImplementedError("TODO: PB0815")


def self_test() -> None:
    assert exc_lookup_int_status({'a': '10'}, 'a') == ('ok', 10)
    assert exc_lookup_int_status({}, 'a') == ('missing', None)
    assert exc_lookup_int_status({'a': 'x'}, 'a') == ('invalid', None)
