"""
PB0423 — 특정 인덱스부터 문자

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(text)라고 가정하고 for와 range(start, len(text))로 start부터 끝까지 문자를 리스트로 반환한다.

연습 초점
---------
유효한 컬렉션 인덱스에서 시작하는 range

구현할 함수
-----------
def characters_from_index(text: str, start: int) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- characters_from_index('python', 3) == ['h', 'o', 'n']
- characters_from_index('abc', 3) == []
- characters_from_index('', 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0423 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def characters_from_index(text: str, start: int) -> list[str]:
    raise NotImplementedError("TODO: PB0423")


def self_test() -> None:
    assert characters_from_index('python', 3) == ['h', 'o', 'n']
    assert characters_from_index('abc', 3) == []
    assert characters_from_index('', 0) == []
