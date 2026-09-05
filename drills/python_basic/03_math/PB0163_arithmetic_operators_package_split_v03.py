"""
PB0163 — 상자와 낱개 나누기

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
items를 package_size로 나눈 온전한 상자 수와 남은 낱개 수를 반환하세요. package_size는 양수입니다.

연습 초점
---------
몫 //와 나머지 %의 역할

구현할 함수
-----------
def split_into_packages(items: int, package_size: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- split_into_packages(17, 5) == (3, 2)
- split_into_packages(0, 4) == (0, 0)
- split_into_packages(5, 5) == (1, 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0163 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_into_packages(items: int, package_size: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0163")


def self_test() -> None:
    assert split_into_packages(17, 5) == (3, 2)
    assert split_into_packages(0, 4) == (0, 0)
    assert split_into_packages(5, 5) == (1, 0)
