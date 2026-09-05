"""
PB0667 — 쉼표 태그를 set으로

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
쉼표로 나눈 각 조각의 앞뒤 공백을 제거하고 빈 태그를 제외해 반환한다.

연습 초점
---------
split, strip, 조건부 set comprehension

구현할 함수
-----------
def set_parse_tags(text: str) -> set[str]:

예시 및 필수 테스트
-------------------
- set_parse_tags('python, api,python') == {'python', 'api'}
- set_parse_tags('') == set()
- set_parse_tags(' a, , b ') == {'a', 'b'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0667 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_parse_tags(text: str) -> set[str]:
    raise NotImplementedError("TODO: PB0667")


def self_test() -> None:
    assert set_parse_tags('python, api,python') == {'python', 'api'}
    assert set_parse_tags('') == set()
    assert set_parse_tags(' a, , b ') == {'a', 'b'}
