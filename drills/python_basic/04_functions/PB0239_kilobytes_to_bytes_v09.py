"""
PB0239 — 킬로바이트 변환

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
1KB를 1024바이트로 계산해 바이트 수를 반환한다.

연습 초점
---------
정수 반환 함수를 정확한 시그니처로 선언

구현할 함수
-----------
def kilobytes_to_bytes(kilobytes: int) -> int:

예시 및 필수 테스트
-------------------
- kilobytes_to_bytes(2) == 2048
- kilobytes_to_bytes(0) == 0
- kilobytes_to_bytes(1024) == 1048576

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0239 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def kilobytes_to_bytes(kilobytes: int) -> int:
    raise NotImplementedError("TODO: PB0239")


def self_test() -> None:
    assert kilobytes_to_bytes(2) == 2048
    assert kilobytes_to_bytes(0) == 0
    assert kilobytes_to_bytes(1024) == 1048576
