"""
PB0357 — 파일 크기 라벨

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
0 미만 invalid, 1024 미만 B, 1048576 미만 KB, 그 이상 MB를 반환한다.

연습 초점
---------
특수 음수와 크기 경계의 검사 순서

구현할 함수
-----------
def file_size_label(bytes_size: int) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- file_size_label(-1) == 'invalid'
- file_size_label(1023) == 'B'
- file_size_label(1048576) == 'MB'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0357 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def file_size_label(bytes_size: int) -> str:
    raise NotImplementedError("TODO: PB0357")


def self_test() -> None:
    assert file_size_label(-1) == 'invalid'
    assert file_size_label(1023) == 'B'
    assert file_size_label(1048576) == 'MB'
