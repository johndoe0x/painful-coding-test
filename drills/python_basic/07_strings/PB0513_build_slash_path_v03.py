"""
PB0513 — 경로 조각 연결하기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 part에는 슬래시가 없다고 가정하고 '/'로 연결한 절대 경로를 만들며 빈 parts는 '/'를 반환한다.

연습 초점
---------
고정 접두사와 반복되는 구분자 결합을 처리한다.

구현할 함수
-----------
def build_path(parts: list[str]) -> str:

예시 및 필수 테스트
-------------------
- build_path(['users', 'ada']) == '/users/ada'
- build_path(['tmp']) == '/tmp'
- build_path([]) == '/'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0513 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def build_path(parts: list[str]) -> str:
    raise NotImplementedError("TODO: PB0513")


def self_test() -> None:
    assert build_path(['users', 'ada']) == '/users/ada'
    assert build_path(['tmp']) == '/tmp'
    assert build_path([]) == '/'
