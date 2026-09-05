"""
PB0137 — 좌표 문자열 파싱

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
'x,y' 형식 문자열을 쉼표로 나누고 두 값을 int로 변환하세요.

연습 초점
---------
분리 후 여러 필드 캐스팅

구현할 함수
-----------
def cast_coordinate(text: str) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- cast_coordinate('3,4') == (3, 4)
- cast_coordinate('0,0') == (0, 0)
- cast_coordinate('-1, 2') == (-1, 2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0137 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_coordinate(text: str) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0137")


def self_test() -> None:
    assert cast_coordinate('3,4') == (3, 4)
    assert cast_coordinate('0,0') == (0, 0)
    assert cast_coordinate('-1, 2') == (-1, 2)
