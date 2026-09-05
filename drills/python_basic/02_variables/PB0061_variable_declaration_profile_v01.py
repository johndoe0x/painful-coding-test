"""
PB0061 — 프로필 변수 선언

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
name과 age를 각각 명확한 변수에 담은 뒤 {'name': name, 'age': age}를 반환하세요.

연습 초점
---------
값을 이름 있는 변수에 저장

구현할 함수
-----------
def build_profile(name: str, age: int) -> dict[str, object]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- build_profile('Ada', 36) == {'name': 'Ada', 'age': 36}
- build_profile('', 0) == {'name': '', 'age': 0}
- build_profile('Lin', 1) == {'name': 'Lin', 'age': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0061 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def build_profile(name: str, age: int) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0061")


def self_test() -> None:
    assert build_profile('Ada', 36) == {'name': 'Ada', 'age': 36}
    assert build_profile('', 0) == {'name': '', 'age': 0}
    assert build_profile('Lin', 1) == {'name': 'Lin', 'age': 1}
