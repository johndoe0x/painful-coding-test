"""
PB0104 — 레코드 언패킹

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
record를 name, age, active에 한 번에 할당하고 '<name>:<age>:<active>' 문자열을 반환하세요.

연습 초점
---------
고정 길이 tuple의 구조 분해

구현할 함수
-----------
def unpack_user_record(record: tuple[str, int, bool]) -> str:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- unpack_user_record(('Ada', 36, True)) == 'Ada:36:True'
- unpack_user_record(('', 0, False)) == ':0:False'
- unpack_user_record(('A', 1, True)) == 'A:1:True'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0104 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unpack_user_record(record: tuple[str, int, bool]) -> str:
    raise NotImplementedError("TODO: PB0104")


def self_test() -> None:
    assert unpack_user_record(('Ada', 36, True)) == 'Ada:36:True'
    assert unpack_user_record(('', 0, False)) == ':0:False'
    assert unpack_user_record(('A', 1, True)) == 'A:1:True'
