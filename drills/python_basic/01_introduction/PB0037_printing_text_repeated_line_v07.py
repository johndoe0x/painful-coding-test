"""
PB0037 — 한 줄 반복 출력

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
text를 count줄로 반복해 줄바꿈으로 결합하세요. count가 0이면 빈 문자열입니다.

연습 초점
---------
반복되는 출력 줄 구성

구현할 함수
-----------
def repeat_output_line(text: str, count: int) -> str:

예시 및 필수 테스트
-------------------
- repeat_output_line('go', 3) == 'go\\ngo\\ngo'
- repeat_output_line('go', 0) == ''
- repeat_output_line('', 2) == '\\n'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0037 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_output_line(text: str, count: int) -> str:
    raise NotImplementedError("TODO: PB0037")


def self_test() -> None:
    assert repeat_output_line('go', 3) == 'go\ngo\ngo'
    assert repeat_output_line('go', 0) == ''
    assert repeat_output_line('', 2) == '\n'
