"""
PB0259 — RGB 색상 혼합

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 RGB 채널 쌍에 대해 (첫 채널 + 둘째 채널) // 2로 소수 부분을 버린 정수 평균을 구해 tuple로 반환한다.

연습 초점
---------
채널별 합에 정수 나눗셈을 적용

구현할 함수
-----------
def blend_rgb(r1: int, g1: int, b1: int, r2: int, g2: int, b2: int) -> tuple[int, int, int]:

예시 및 필수 테스트
-------------------
- blend_rgb(0, 0, 0, 100, 50, 200) == (50, 25, 100)
- blend_rgb(255, 255, 255, 255, 255, 255) == (255, 255, 255)
- blend_rgb(1, 2, 3, 2, 3, 4) == (1, 2, 3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0259 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def blend_rgb(r1: int, g1: int, b1: int, r2: int, g2: int, b2: int) -> tuple[int, int, int]:
    raise NotImplementedError("TODO: PB0259")


def self_test() -> None:
    assert blend_rgb(0, 0, 0, 100, 50, 200) == (50, 25, 100)
    assert blend_rgb(255, 255, 255, 255, 255, 255) == (255, 255, 255)
    assert blend_rgb(1, 2, 3, 2, 3, 4) == (1, 2, 3)
