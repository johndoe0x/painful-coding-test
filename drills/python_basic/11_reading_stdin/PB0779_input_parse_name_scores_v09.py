"""
PB0779 — 이름별 점수 입력

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
쉼표로 구분된 'name=score' 항목을 딕셔너리로 반환한다. 빈 text는 빈 딕셔너리다.

연습 초점
---------
반복되는 복합 필드 파싱

구현할 함수
-----------
def input_parse_name_scores(text: str) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- input_parse_name_scores('Ada=90,Kim=80') == {'Ada': 90, 'Kim': 80}
- input_parse_name_scores('') == {}
- input_parse_name_scores('A=-1') == {'A': -1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0779 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_name_scores(text: str) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0779")


def self_test() -> None:
    assert input_parse_name_scores('Ada=90,Kim=80') == {'Ada': 90, 'Kim': 80}
    assert input_parse_name_scores('') == {}
    assert input_parse_name_scores('A=-1') == {'A': -1}
