"""
PB0034 — 라벨 폭 맞추기

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
label을 width칸 안에서 오른쪽 정렬하세요. 이미 길면 자르지 마세요.

연습 초점
---------
문자열 정렬 포맷

구현할 함수
-----------
def align_label(label: str, width: int) -> str:

예시 및 필수 테스트
-------------------
- align_label('ID', 5) == '   ID'
- align_label('', 3) == '   '
- align_label('Python', 3) == 'Python'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0034 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def align_label(label: str, width: int) -> str:
    raise NotImplementedError("TODO: PB0034")


def self_test() -> None:
    assert align_label('ID', 5) == '   ID'
    assert align_label('', 3) == '   '
    assert align_label('Python', 3) == 'Python'
