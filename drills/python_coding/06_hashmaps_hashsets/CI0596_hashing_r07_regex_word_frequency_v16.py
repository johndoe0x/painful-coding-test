"""
CI0596 — 정규표현식 단어 빈도 — 반복 세트 7

Chapter: Hashmaps and Hashsets
Seed: 30 / 40
Variant: 16 / 20
Time cap: 240 seconds
Source checks: re_call, counter_call

문제
----
re로 영문자와 숫자로 이루어진 단어를 추출하고 소문자 Counter 빈도를 반환하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 7이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
re tokenization과 Counter

구현할 함수
-----------
def hashing_r07_regex_word_frequency(text: str) -> dict[str, int]:

필수 구현 방식
--------------
- re 모듈의 정규표현식 API를 사용한다.
- collections.Counter를 사용한다.

예시 및 필수 테스트
-------------------
- hashing_r07_regex_word_frequency('Hi, hi! 42') == {'hi': 2, '42': 1}
- hashing_r07_regex_word_frequency('') == {}
- hashing_r07_regex_word_frequency('A_b') == {'a': 1, 'b': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0596 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r07_regex_word_frequency(text: str) -> dict[str, int]:
    raise NotImplementedError("TODO: CI0596")


def self_test() -> None:
    assert hashing_r07_regex_word_frequency('Hi, hi! 42') == {'hi': 2, '42': 1}
    assert hashing_r07_regex_word_frequency('') == {}
    assert hashing_r07_regex_word_frequency('A_b') == {'a': 1, 'b': 1}
