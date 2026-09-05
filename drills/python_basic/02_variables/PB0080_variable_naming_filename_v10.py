"""
PB0080 — 파일 이름 구성

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
'<project_name>.<file_extension>' 형식으로 반환하되 extension 앞의 점은 입력에 없다고 가정하세요.

연습 초점
---------
역할이 분명한 문자열 변수명

구현할 함수
-----------
def build_export_filename(project_name: str, file_extension: str) -> str:

예시 및 필수 테스트
-------------------
- build_export_filename('report', 'csv') == 'report.csv'
- build_export_filename('', '') == '.'
- build_export_filename('data', 'json') == 'data.json'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0080 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def build_export_filename(project_name: str, file_extension: str) -> str:
    raise NotImplementedError("TODO: PB0080")


def self_test() -> None:
    assert build_export_filename('report', 'csv') == 'report.csv'
    assert build_export_filename('', '') == '.'
    assert build_export_filename('data', 'json') == 'data.json'
