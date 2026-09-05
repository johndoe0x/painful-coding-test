"""
PB0653 — 프로필 tuple 풀어 쓰기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
(name, age)를 언패킹해 '<name> is <age>' 형식의 문자열을 반환한다.

연습 초점
---------
tuple 원소를 의미 있는 지역 변수로 언패킹한다.

구현할 함수
-----------
def profile_sentence(profile: tuple[str, int]) -> str:

예시 및 필수 테스트
-------------------
- profile_sentence(('Ada', 36)) == 'Ada is 36'
- profile_sentence(('Kim', 0)) == 'Kim is 0'
- profile_sentence(('', 5)) == ' is 5'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0653 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def profile_sentence(profile: tuple[str, int]) -> str:
    raise NotImplementedError("TODO: PB0653")


def self_test() -> None:
    assert profile_sentence(('Ada', 36)) == 'Ada is 36'
    assert profile_sentence(('Kim', 0)) == 'Kim is 0'
    assert profile_sentence(('', 5)) == ' is 5'
