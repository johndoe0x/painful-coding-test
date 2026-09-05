"""
PB0755 — 명령어와 인자 분리

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
strip 후 공백으로 나눠 첫 단어를 command, 나머지를 args로 반환한다. 내용이 없으면 ('', [])를 반환한다.

연습 초점
---------
입력 token 목록의 head와 tail 분리

구현할 함수
-----------
def line_parse_command(line: str) -> tuple[str, list[str]]:

예시 및 필수 테스트
-------------------
- line_parse_command('add 10 20') == ('add', ['10', '20'])
- line_parse_command('   ') == ('', [])
- line_parse_command('quit') == ('quit', [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0755 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_parse_command(line: str) -> tuple[str, list[str]]:
    raise NotImplementedError("TODO: PB0755")


def self_test() -> None:
    assert line_parse_command('add 10 20') == ('add', ['10', '20'])
    assert line_parse_command('   ') == ('', [])
    assert line_parse_command('quit') == ('quit', [])
