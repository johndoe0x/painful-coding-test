"""
PB0028 — 선행 단계 배치

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
prerequisites를 주어진 순서로 배치하고 마지막에 task를 붙이세요.

연습 초점
---------
선행 작업과 본 작업의 순서

구현할 함수
-----------
def dependency_schedule(task: str, prerequisites: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- dependency_schedule('deploy', ['test', 'build']) == ['test', 'build', 'deploy']
- dependency_schedule('run', []) == ['run']
- dependency_schedule('', ['prepare']) == ['prepare', '']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0028 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dependency_schedule(task: str, prerequisites: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0028")


def self_test() -> None:
    assert dependency_schedule('deploy', ['test', 'build']) == ['test', 'build', 'deploy']
    assert dependency_schedule('run', []) == ['run']
    assert dependency_schedule('', ['prepare']) == ['prepare', '']
