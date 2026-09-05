"""
PB0042 — 없는 딕셔너리 키 오류 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 mapping[key]로 직접 조회해 없는 키에서 KeyError가 납니다. key가 있으면 값을, 없으면 default를 반환하도록 고치세요.

연습 초점
---------
직접 인덱싱 대신 누락 키의 기본값을 안전하게 처리

구현할 함수
-----------
def corrected_dictionary_default(mapping: dict[str, int], key: str, default: int) -> int:

예시 및 필수 테스트
-------------------
- corrected_dictionary_default({'a': 1}, 'a', 9) == 1
- corrected_dictionary_default({'a': 1}, 'x', 9) == 9
- corrected_dictionary_default({}, '', 0) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0042 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def corrected_dictionary_default(mapping: dict[str, int], key: str, default: int) -> int:
    return mapping[key]


def self_test() -> None:
    assert corrected_dictionary_default({'a': 1}, 'a', 9) == 1
    assert corrected_dictionary_default({'a': 1}, 'x', 9) == 9
    assert corrected_dictionary_default({}, '', 0) == 0
