"""
PB0309 — 기본 접두부 길이

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
text의 앞 size글자를 반환하며 size 생략 시 한 글자를 사용한다.

연습 초점
---------
슬라이스 크기 기본 인자

구현할 함수
-----------
def prefix_with_default_size(text: str, size: int = 1) -> str:

예시 및 필수 테스트
-------------------
- prefix_with_default_size('python') == 'p'
- prefix_with_default_size('python', 3) == 'pyt'
- prefix_with_default_size('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0309 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def prefix_with_default_size(text: str, size: int = 1) -> str:
    raise NotImplementedError("TODO: PB0309")


def self_test() -> None:
    assert prefix_with_default_size('python') == 'p'
    assert prefix_with_default_size('python', 3) == 'pyt'
    assert prefix_with_default_size('') == ''
