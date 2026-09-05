"""
PB0737 — 빈 문자열 value 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
정확히 빈 문자열인 value를 제거한다. 공백 문자열은 유지한다.

연습 초점
---------
문자열 동등 비교로 선택 제거

구현할 함수
-----------
def dict_remove_empty_text(mapping: dict[str, str]) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- dict_remove_empty_text({'a': '', 'b': 'x'}) == {'b': 'x'}
- dict_remove_empty_text({}) == {}
- dict_remove_empty_text({'space': ' '}) == {'space': ' '}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0737 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_remove_empty_text(mapping: dict[str, str]) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0737")


def self_test() -> None:
    assert dict_remove_empty_text({'a': '', 'b': 'x'}) == {'b': 'x'}
    assert dict_remove_empty_text({}) == {}
    assert dict_remove_empty_text({'space': ' '}) == {'space': ' '}
