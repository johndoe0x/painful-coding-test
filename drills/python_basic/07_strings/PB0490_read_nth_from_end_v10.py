"""
PB0490 — 뒤에서 n번째 글자

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
n이 1 이상이고 text 길이 이하이면 뒤에서 n번째 글자를, 아니면 None을 반환한다.

연습 초점
---------
1부터 시작하는 위치를 음수 인덱스로 변환한다.

구현할 함수
-----------
def nth_character_from_end(text: str, n: int) -> str | None:

예시 및 필수 테스트
-------------------
- nth_character_from_end('python', 1) == 'n'
- nth_character_from_end('python', 3) == 'h'
- nth_character_from_end('python', 0) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0490 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def nth_character_from_end(text: str, n: int) -> str | None:
    raise NotImplementedError("TODO: PB0490")


def self_test() -> None:
    assert nth_character_from_end('python', 1) == 'n'
    assert nth_character_from_end('python', 3) == 'h'
    assert nth_character_from_end('python', 0) is None
