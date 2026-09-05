"""
PB0518 — 빈 조각을 건너뛰어 연결하기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
빈 문자열을 제외한 parts만 separator로 연결한다.

연습 초점
---------
결합 대상 선별과 구분자 위치 관리를 함께 연습한다.

구현할 함수
-----------
def concatenate_nonempty(parts: list[str], separator: str) -> str:

예시 및 필수 테스트
-------------------
- concatenate_nonempty(['a', '', 'b'], ':') == 'a:b'
- concatenate_nonempty(['', ''], '-') == ''
- concatenate_nonempty(['x'], '/') == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0518 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def concatenate_nonempty(parts: list[str], separator: str) -> str:
    raise NotImplementedError("TODO: PB0518")


def self_test() -> None:
    assert concatenate_nonempty(['a', '', 'b'], ':') == 'a:b'
    assert concatenate_nonempty(['', ''], '-') == ''
    assert concatenate_nonempty(['x'], '/') == 'x'
