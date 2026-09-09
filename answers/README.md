# 공개 답안 이력

검증한 답안을 문제별·소스 버전별로 저장하는 폴더입니다.
자동으로 기존 풀이를 일괄 업로드하지 않으며, 아래 명령에서 지정한 문제만 올립니다.

```bash
cd drills
python3 -B submit_answer.py PB0001
```

각 버전에는 두 파일이 함께 올라갑니다.

```text
answers/PB0001/<소스 SHA-256>/solution.py
answers/PB0001/<소스 SHA-256>/result.json
```

같은 코드는 중복 커밋을 만들지 않고, 다른 코드는 새 버전으로 남깁니다.
결과는 로컬 공개 예시·self_test·필수 Python 문법 검사이며 독립 서버 채점이나
암기 여부 인증은 아닙니다. 코드와 결과 요약은 공개적으로 읽을 수 있습니다.

[오프라인 저장·재시도·설정 안내](../drills/docs/submit-answers.md)
