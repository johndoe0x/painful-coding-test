# Python Coding Interview 800

코딩테스트에서 Python 문법·자료구조·표준 라이브러리를 문서 검색 없이 빠르고 정확하게 쓰는 자동화 드릴입니다.
배운 도구를 빈 화면에서 재구현하는 것이 목표이며, 알고리즘 패턴 학습과 C 레벨 인증은 후속 NeetCode 250에서 진행합니다.

## 구성

- 8개 챕터
- 40개 기본 계약 복습 트랙
- 기본형 40개와 챕터별 사용법 변형·반복 훈련
- 총 800개 문제와 2,400개 필수 assert
- 목적을 벗어났던 알고리즘 문제 48개를 Python 도구 사용법 드릴로 교체
- 48개 모두 150~300초 범위이며, ID는 유지하고 함수·파일 이름을 새 과제에 맞춤
- 함수 이름을 제거한 테스트 AST로 중복을 집계하며, 이를 고유 알고리즘 수로 부르지 않음
- 특정 문법·표준 라이브러리 API 사용은 AST 기반 학습 보조 검사로 확인

```text
01_sorting
02_pythonic_code
03_lists
04_stacks_queues
05_2d_lists
06_hashmaps_hashsets
07_heaps_priority_queues
08_sorted_dicts_sets
```

전체 문제 링크는 [INDEX.md](INDEX.md)에서 확인합니다.

## 품질 기준

예전 v02~v20은 문제 설명에서 보조 알고리즘을 요구하면서도 실제 함수 시그니처와 테스트는 baseline을 반복했습니다. 현재 문제은행은 각 파일의 문제, 함수 시그니처, 세 테스트와 필수 API 검사가 같은 계약을 가리키도록 다시 생성했습니다.

반복은 인출 속도와 정확성을 높이기 위한 훈련입니다. 전체 800개를 10문제 단위로 연습하고 최초 통과율·소요시간·반복되는 Python 오류를 기록합니다. 같은 계약이라는 이유만으로 훈련 대상에서 제외하지 않습니다. 이전의 '핵심 240개 + 선택 560개' 분류는 철회했습니다.

48개에서는 정렬 key·동률 안정성, unpacking·iterator·yield, 얕은/행별 복사, deque 연산, Counter·dict·set, heap 결합 연산, bisect의 key·lo·hi를 연습합니다. 기존에 보강한 예시 오류·반례 검사는 유지했습니다.
자세한 변경은 [목적 교정 보고서](../docs/reviews/2026-09-05-python-coding-purpose-correction.md)에 있습니다.
항상 [INDEX.md](INDEX.md)에서 현재 파일을 열고 파일 상단의 문제와 시그니처를 기준으로 풀이하세요.

세 공개 assert는 예시이자 최소 회귀 검사입니다. 모든 유효 입력을 검증하는 숨은 테스트나 완전한 oracle은 아닙니다. AST 검사는 API 이름을 썼다는 제한적인 근거이며, 요구한 알고리즘·시간복잡도·lazy 소비·메모리 상한을 증명하지 않습니다. 완료 전에는 직접 추가 경계 사례를 만들고 복잡도를 설명하세요.

## 표준 라이브러리 범위

다음 도구를 다루는 전용 문제와 학습 보조 source check가 있습니다.

- `collections.Counter`, `defaultdict`, `deque`
- `heapq`
- `bisect`
- `itertools`
- `functools.cache`, `lru_cache`, `cmp_to_key`
- `math.gcd`, `lcm`, `isqrt`, `ceil`, `inf`
- `operator.itemgetter`
- `re`
- `pathlib.Path`, `json.loads`, `csv.reader`
- `iter`, `next`, `yield`

`pathlib`, `json`, `csv` 문제는 경로 구조와 문자열 데이터 parsing을 다룹니다. 실제 임시 파일 생성·읽기·쓰기·인코딩·원자적 저장은 별도의 파일·JSON 실습 문제은행에서 다루는 것이 적합합니다.

## 풀이 방법

1. 문제 파일에서 문제·함수 시그니처·필수 구현 방식·테스트 세 개를 읽습니다.
2. 필요한 import부터 기억에서 직접 작성합니다.
3. `NotImplementedError`를 실제 구현으로 교체합니다.
4. 파일 마지막에 시간·공간복잡도를 주석으로 적습니다.
5. 저장소 루트에서 strict runner를 실행합니다.

기본 목표는 150초, 여러 도구를 조합하는 드릴은 최대 300초입니다. 처음 보는 API는 먼저 학습한 뒤 복습 때 시간을 측정합니다.
한 배치 10개를 풀고 최초 통과율 85% 이상, 무작위 cold audit 90% 이상, 문서 검색 없이 도구를 사용할 수 있는지를 확인합니다.

```bash
# 저장소 루트에서 실행
python3 -B -m python_coding CI0005 --strict
```

함수의 `print()`는 `[public_example_1 stdout]`처럼 표시되고, `logging.debug/info/warning()`은 `[stderr/log]`에 표시됩니다. PASS한 실행은 `proofs/CI0005.json`에 소스 해시와 실행 출력이 기록됩니다.

## 검증

```bash
python3 -B python_coding/validate_bank.py
python3 -B python_coding/validate_bank.py --strict-user-code
python3 -B -m unittest discover -s tests -p 'test_coding_quality.py'
python3 -B -m unittest discover -s tests -p 'test_fluency_catalog.py'
```

일반 검증은 생성된 계약·공개 호출 인수·문서/테스트 일치·중복을 검사하고 사용자가 편집 중인 문법 오류를 별도 집계합니다. `--strict-user-code`는 그 오류까지 실패로 처리합니다. 회귀 테스트는 유지한 주요 계약 수정과 48개 Python 드릴의 공개·추가 예시, 필수 API 사용, 잘못된 API 선택을 확인합니다. 모든 유효 입력에 대한 완전한 채점기는 아닙니다. 최신 수치는 `validate_bank.py` 출력과 [재생성 보고서](REGENERATION_REPORT.md)를 확인하세요.

## 안전한 재생성

```bash
python3 -B python_coding/regenerate_variants.py
```

재생성 상태는 `generated_manifest.json`으로 추적합니다. 계약이 같은 사용자 파일은 그대로 유지하고, 변경된 계약에 사용자 코드가 있으면 `_preserved_answers/`에 원본 전체를 보관한 뒤 새 starter를 생성합니다. manifest가 없으면 TODO가 남아 있다는 이유만으로 사용자 작업을 pristine으로 판단하지 않습니다. 작업 중 임시 stage와 backup은 저장소의 `.tmp/` 아래에만 만들고 해당 실행이 만든 경로만 정리합니다. 동일 상태에서 다시 실행하면 `unchanged=800`이 출력됩니다.

기존의 저품질 초기 생성기 `generate_bank.py`는 새 문제은행을 덮어쓰지 못하도록 비활성화했습니다.
