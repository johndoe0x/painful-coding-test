"""
PB0292 — 전역 접두사와 지역 접두사

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
GLOBAL_TEXT_PREFIX와 지역 매개변수 local_prefix를 각각 text 앞에 붙여 (전역 접두사 결과, 지역 접두사 결과)를 반환한다.

연습 초점
---------
모듈 전역 문자열과 호출별 지역 문자열을 나란히 사용

구현할 함수
-----------
def format_with_global_and_local_prefix(text: str, local_prefix: str) -> tuple[str, str]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- format_with_global_and_local_prefix('data', 'LOCAL:') == ('GLOBAL:data', 'LOCAL:data')
- format_with_global_and_local_prefix('', '#') == ('GLOBAL:', '#')
- format_with_global_and_local_prefix('x', '') == ('GLOBAL:x', 'x')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0292 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_TEXT_PREFIX = 'GLOBAL:'


def format_with_global_and_local_prefix(text: str, local_prefix: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0292")


def self_test() -> None:
    assert format_with_global_and_local_prefix('data', 'LOCAL:') == ('GLOBAL:data', 'LOCAL:data')
    assert format_with_global_and_local_prefix('', '#') == ('GLOBAL:', '#')
    assert format_with_global_and_local_prefix('x', '') == ('GLOBAL:x', 'x')
