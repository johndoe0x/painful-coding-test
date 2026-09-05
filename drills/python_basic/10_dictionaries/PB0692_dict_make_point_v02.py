"""
PB0692 — 좌표 딕셔너리

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
x와 y 좌표를 같은 이름의 key에 담아 반환한다.

연습 초점
---------
매개변수에서 key-value 구성

구현할 함수
-----------
def dict_make_point(x: int, y: int) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_make_point(2, 3) == {'x': 2, 'y': 3}
- dict_make_point(0, 0) == {'x': 0, 'y': 0}
- dict_make_point(-1, 5) == {'x': -1, 'y': 5}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0692 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_make_point(x: int, y: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0692")


def self_test() -> None:
    assert dict_make_point(2, 3) == {'x': 2, 'y': 3}
    assert dict_make_point(0, 0) == {'x': 0, 'y': 0}
    assert dict_make_point(-1, 5) == {'x': -1, 'y': 5}
