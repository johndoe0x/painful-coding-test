"""
PB0068 — 로그인 상태 변수

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
username과 authenticated를 변수로 선언하고 인증됐으면 '<username>:online', 아니면 '<username>:offline'을 반환하세요.

연습 초점
---------
입력 변수와 파생 결과 연결

구현할 함수
-----------
def declare_login_state(username: str, authenticated: bool) -> str:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_login_state('ada', True) == 'ada:online'
- declare_login_state('', False) == ':offline'
- declare_login_state('root', False) == 'root:offline'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0068 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_login_state(username: str, authenticated: bool) -> str:
    raise NotImplementedError("TODO: PB0068")


def self_test() -> None:
    assert declare_login_state('ada', True) == 'ada:online'
    assert declare_login_state('', False) == ':offline'
    assert declare_login_state('root', False) == 'root:offline'
