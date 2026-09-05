# Python Basic 820

Python 문법과 기본 자료구조를 생각과 동시에 구현하는 자동화 훈련용 문제은행입니다.

## 구성

- 12개 챕터
- 82개 seed 주제
- seed당 10개의 주제별 맞춤 문제
- 총 820개 `.py` 문제
- 모범 답안은 포함하지 않으며, 사용자가 작성한 함수는 재생성 때 보존

```text
01_introduction
02_variables
03_math
04_functions
05_conditionals
06_loops
07_strings
08_lists
09_sets
10_dictionaries
11_reading_stdin
12_exception_handling
```

전체 문제 링크는 [INDEX.md](INDEX.md)에서 확인합니다.

2026-09-05 재평가 결과와 학습 순서는 [통합 학습 경로](../STUDY_PATH.md)와
[문제은행 리뷰](../docs/reviews/2026-09-05-problem-bank-review.md)에 있습니다.
이 은행은 기초 문법을 배운 뒤 속도를 익히는 드릴입니다. 처음 Python을 배우는
경우에는 각 주제의 설명을 먼저 읽고 v01로 진단한 뒤 필요한 변형을 선택하세요.
초반에도 함수·리스트·딕셔너리를 사용하므로 파일 순서만 따라가면 선행 지식이
자동으로 설명되는 입문 강의는 아닙니다. 제한시간은 복습 목표로 사용합니다.

## 풀이 방법

1. 문제 파일 하나를 연다.
2. docstring의 문제·연습 초점·함수 시그니처·검증식 세 개를 읽는다.
3. 문제에 표시된 제한시간으로 타이머를 시작한다.
4. `NotImplementedError`를 실제 구현으로 교체한다. `Code Errors` 문제는 일부러 틀린 starter를 고친다.
5. 포함된 `self_test()` 검증식 세 개를 통과시킨다.
6. 답을 보며 타이핑한 시도는 완료로 세지 않는다.

이 문제들은 개별 답안을 장기 암기하는 문제가 아닙니다. 같은 Python 동작을 여러 형태로 빠르게 재구현해 자동화하는 드릴입니다.

## 문제 설계 원칙

고정된 변형 이름을 82개 주제에 반복 적용하지 않습니다. 각 주제마다 그 개념을 실제로 연습하는 문제 10개를 별도로 구성했습니다.

예를 들어 `Hello, World`에서는 문자열 리터럴, 이름 매개변수, 인사 리스트, 구두점, 조건 분기를 연습합니다. `String Slicing`에서는 prefix·suffix·구간·step·분할을, `List Pop`에서는 끝·처음·특정 인덱스 제거와 원본 보존을, `Multiple Except Blocks`에서는 오류 유형별 상태 반환을 연습합니다.

820개 문제는 모두 서로 다른 함수 이름, 문제 설명, 연습 초점과 테스트 묶음을 가집니다. 모든 문제에는 정상·빈 값·경계값 중 적용 가능한 세 가지 구체 검증식이 들어 있습니다.

함수명과 설명이 다르다는 것만으로 새로운 개념이라고 판정하지 않습니다.
재평가는 함수 이름을 정규화한 테스트와 필수 구현 방식도 비교합니다.
OR/AND 문제의 검증식에는 양쪽 조건을 각각 독립적으로 만족하는 경우와 경계값을
함께 넣고, 원본 보존이 요구되는 문제는 호출 후 입력도 확인합니다.

## 검증

문제 수, ID 연속성, Python 문법, 필수 메타데이터뿐 아니라 함수 이름·문제 설명·테스트 묶음의 중복도 검사합니다.

```bash
python3 -B -m python_basic.catalog.validate_catalog
python3 -B python_basic/validate_bank.py
python3 -B python_basic/validate_bank.py --strict-user-code
```

첫 명령은 820개 카탈로그의 중복과 계약을 검사합니다. 두 번째 명령은 문제은행 구조를 검사하면서 편집 중인 사용자 코드의 문법 오류를 별도 집계합니다. `--strict-user-code`는 그 오류까지 전체 실패로 처리합니다.

개인적으로 복사해 둔 풀이 파일은 삭제하거나 자동 병합하지 않습니다. 검증기는
카탈로그의 공식 820개 경로를 검사하고 추가 파일 수를 따로 출력하며, 실행기는
manifest에 등록된 문제 경로를 사용합니다. `_preserved_answers/`의 옛 답안은
현재 문제로 실행하지 않습니다. 정적 소스 검사는 지정 문법의 존재를 확인하는
보조 검사이며 알고리즘의 일반적인 정확성이나 시간복잡도를 증명하지는 않습니다.

## 답안 실행과 증명

반복 runner 코드는 문제 파일에 넣지 않습니다. 저장소 루트에서 패키지 명령으로 실행하면 첫 줄에 `PASS` 또는 `FAIL`이 출력되고, 성공 시 proof 영수증이 생성됩니다.

따라서 문제 파일을 직접 실행하는 대신 아래 공통 명령을 사용합니다.

```bash
# 문제은행 저장소 루트에서 실행
python3 -B -m python_basic PB0001
```

예상 출력:

```text
PASS PB0001
user_output=none
file=python_basic/01_introduction/PB0001_hello_world_exact_message_v01.py
...
receipt=proofs/PB0001.json
```

미완성이거나 테스트가 틀리면 stdout에 `FAIL PB0001`이 출력되고 프로세스 종료 코드는 1입니다.

풀이 함수 안의 `print()`와 `logging.debug/info/warning()`도 숨기지 않습니다. PASS/FAIL을 먼저 출력한 뒤 실행 위치별로 묶어서 보여줍니다.

```text
PASS PB0003
user_output_records=4
USER_OUTPUT_BEGIN
[public_example_1 stdout]
['Hello, Ada!', 'Hello, Lin!']
[self_test stdout]
...
USER_OUTPUT_END
```

공개 예시 세 개를 먼저 실행하고 `self_test()`가 같은 입력을 다시 검사하므로 디버그 출력이 두 번 보이는 것은 정상입니다. 로그는 `[... stderr/log]` 아래 표시되며 runner가 실행 중에는 DEBUG 이상 레벨을 모두 보여줍니다.

공통 실행기를 직접 호출해도 동일합니다.

```bash
python3 run_problem.py PB0001
```

이 명령은 Python 문법, 남아 있는 `NotImplementedError`, docstring 공개 예시를 검사하고 `proofs/PB0001.json` 영수증을 생성합니다.

각 문제에는 이미 seed별 자체 테스트 세 개가 포함됩니다.

```python
def self_test() -> None:
    assert make_message() == "Hello, world!"
    assert len(make_message()) == 13
    assert make_message().endswith("!")
```

그다음 strict 검사를 실행합니다.

```bash
python3 -B -m python_basic PB0001 --strict
python3 -B -m python_basic PB0001 --verify-receipt
```

영수증은 실행 시각, Python 버전, 테스트 결과와 소스 SHA-256을 기록합니다. 로컬 영수증은 해당 코드가 실행됐다는 재현 가능한 증거지만, 누가 직접 작성했는지까지 증명하는 외부 인증은 아닙니다.

문제 설명과 검증식을 다시 생성할 때는 다음 도구를 사용합니다. 같은 계약의 사용자 코드는 파일 전체를 그대로 유지합니다. 생성 형식만 바뀌면 풀이 영역을 합쳐 보존하며, 문제 계약이 달라진 수정 파일은 `_preserved_answers/`에 원본 전체를 먼저 보관합니다. 생성 상태는 `catalog/generated_manifest.json`으로 추적합니다.

```bash
python3 python_basic/regenerate_problems.py
```

초기 생성기 `generate_bank.py`는 기존 답안을 덮어쓰지 않도록 비활성화했습니다.
